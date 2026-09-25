#!/usr/bin/env python3
"""Regression tests for the repo tooling. Stdlib only, no network.

    python3 tools/test_tools.py

Locks in the behaviours that took real debugging to get right:

  classification  fixture text routes to the expected section
  ranking         known-ambiguous material stays in the top-3
  briefs          brief detection by filename and by title
  slugs           generic filenames never become the slug
  dates           date sources in priority order
  sync-daily      stray relocation, #daily regeneration, idempotency

The sync-daily cases run against a throwaway repo copy in a temp dir, so the
real repository is never touched.
"""

from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
REPO = TOOLS.parent


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, TOOLS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


classify = load("classify-material")
sync = load("sync-daily")


class TestClassification(unittest.TestCase):
    """Content routes to the section a human curator would choose."""

    @classmethod
    def setUpClass(cls):
        cls.idf = classify.pattern_idf(REPO)

    def route(self, title: str, body: str) -> str:
        return classify.rank_sections(title, body, self.idf)[0][0]

    def test_clear_signal_routes_correctly(self):
        cases = {
            "auto": ("特斯拉 FSD 入华与国产智驾竞争格局",
                     "对比 Momenta 小鹏 华为 ADS 的端到端方案，Robotaxi 与激光雷达成本"),
            "chip": ("国产 GPU 与训练集群互联带宽调研",
                     "华为昇腾 寒武纪 海光 的芯片算力与 NVLink 互联带宽，先进封装 HBM 瓶颈"),
            "truck": ("大型商用货车座舱需求调研",
                      "重卡 卡车司机 用户画像与 干线物流 车队运营 场景，牵引车 主机厂需求"),
            "healthcare": ("医疗信息系统深度调研",
                           "HIS EMR PACS RIS LIS 电子病历与临床 诊疗 数据集成"),
            "embodied": ("人形机器人灵巧手技术路线",
                         "具身智能 世界模型 与 sim2real 仿真到现实 迁移，机械臂抓取"),
            "society": ("中学英语学习方法深度调研",
                        "中学 课程 教学 学习法 与 考试 备考，青少年 教育 方法"),
        }
        for expected, (title, body) in cases.items():
            with self.subTest(expected=expected):
                self.assertEqual(self.route(title, body), expected)

    def test_ambiguous_material_keeps_truth_in_top3(self):
        """Cross-cutting topics: top-1 may vary, but must stay shortlisted."""
        title = "云厂商具身智能战略与可执行落地路径"
        body = ("云厂商 架构师 视角下的 具身智能 机器人 方案选型，"
                "以及 基础设施 部署 与 供应链 协同")
        top3 = [s for s, _, _ in classify.rank_sections(title, body, self.idf)[:3]]
        self.assertIn("embodied", top3)

    def test_confidence_is_normalised(self):
        ranked = classify.rank_sections(
            "芯片半导体晶圆制程光刻机调研", "芯片 半导体 晶圆 制程 光刻 EDA", self.idf)
        total = sum(v for _, v, _ in ranked)
        self.assertAlmostEqual(total, 1.0, places=6)
        self.assertGreater(ranked[0][1], 0.5)

    def test_empty_text_does_not_crash(self):
        ranked = classify.rank_sections("", "", self.idf)
        self.assertEqual(len(ranked), len(classify.SECTIONS))
        self.assertEqual(ranked[0][1], 0.0)


class TestBriefDetection(unittest.TestCase):
    def test_detected_by_filename(self):
        self.assertEqual(classify.detect_brief("evolution-brief-2026-09-26.html", ""), "evolution")
        self.assertEqual(classify.detect_brief("hn-brief-2026-09-26.html", ""), "hn")

    def test_detected_by_title_when_filename_is_generic(self):
        self.assertEqual(
            classify.detect_brief("download.html", "🧬 自进化简报 · 第 121 期"), "evolution")
        self.assertEqual(
            classify.detect_brief("x.html", "Hacker News 每日简报 — 2026年09月26日"), "hn")

    def test_ordinary_report_is_not_a_brief(self):
        self.assertIsNone(
            classify.detect_brief("fsd-china.html", "特斯拉 FSD 入华与国产智驾竞争格局"))


class TestSlugDerivation(unittest.TestCase):
    def test_generic_filenames_never_become_the_slug(self):
        for stem in ("incoming", "report", "index", "untitled", "final", "download"):
            with self.subTest(stem=stem):
                slug, _ = classify.derive_slug(
                    Path(f"/tmp/{stem}.html"), "HuggingFace OpenSource Model Benchmark",
                    "2026-09-25", "ai")
                self.assertNotEqual(slug, stem)
                self.assertTrue(slug)

    def test_meaningful_ascii_filename_is_kept(self):
        slug, needs = classify.derive_slug(
            Path("/tmp/2026-09-24-hf-cross-vendor-models.html"), "任意标题", "2026-09-24", "ai")
        self.assertEqual(slug, "2026-09-24-hf-cross-vendor-models")
        self.assertFalse(needs)

    def test_no_ascii_signal_is_flagged_for_a_human(self):
        slug, needs = classify.derive_slug(
            Path("/tmp/new.html"), "全中文标题没有任何英文", "2026-09-25", "auto")
        self.assertTrue(needs)
        self.assertEqual(slug, "2026-09-25-auto-report")


class TestAccuracyFloor(unittest.TestCase):
    """Locks in the classifier's quality on this repo's own labelled corpus.

    The IDF weighting is what buys ~7 points of top-1 over flat base weights, but
    it is a statistical property with no single fixture that fails without it.
    An accuracy floor on the whole corpus is the only test that catches its loss.
    Measured: top-1 77.3%, top-3 93.2% (flat weights: 70.5% / 91.7%).
    """

    FLOOR_TOP1 = 0.75
    FLOOR_TOP3 = 0.92

    def test_corpus_accuracy_holds(self):
        mapping = classify.indexed_sections(REPO)
        idf = classify.pattern_idf(REPO)
        items = []
        for dirname, actual in mapping.items():
            files = sorted((REPO / "reports" / dirname).glob("*.html"))
            if files:
                items.append((actual,) + classify.extract_text(files[0]))
        self.assertGreaterEqual(len(items), 100, "corpus unexpectedly small")
        top1 = top3 = 0
        for actual, title, body in items:
            order = [s for s, _, _ in classify.rank_sections(title, body, idf)]
            top1 += order[0] == actual
            top3 += actual in order[:3]
        n = len(items)
        self.assertGreaterEqual(top1 / n, self.FLOOR_TOP1,
                                f"top-1 {top1/n:.1%} below floor {self.FLOOR_TOP1:.0%}")
        self.assertGreaterEqual(top3 / n, self.FLOOR_TOP3,
                                f"top-3 {top3/n:.1%} below floor {self.FLOOR_TOP3:.0%}")

    def test_idf_actually_discounts_common_patterns(self):
        """A pattern firing in most reports must weigh less than a rare one."""
        idf = classify.pattern_idf(REPO)
        common = next(p for p, _ in classify.SECTIONS[12][2] if "文化" in p)   # think: 文化
        rare = next(p for p, _ in classify.SECTIONS[2][2] if "商用货车" in p)  # truck
        self.assertLess(idf[common], idf[rare],
                        "IDF weighting is not discounting high-frequency patterns")


class TestDateDerivation(unittest.TestCase):
    def test_prefix_date_wins(self):
        self.assertEqual(
            classify.derive_date(Path("/tmp/2026-08-13-thing.html"), "2020-01-01"), "2026-08-13")

    def test_chinese_date_is_parsed(self):
        self.assertEqual(
            classify.derive_date(Path("/tmp/x.html"), "报告日期：2026年9月5日"), "2026-09-05")

    def test_iso_date_in_body_is_a_fallback(self):
        self.assertEqual(
            classify.derive_date(Path("/tmp/x.html"), "数据截止 2026-09-20 结束"), "2026-09-20")


class TestSyncDaily(unittest.TestCase):
    """Runs sync-daily against a temp repo copy; never touches the real one."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        (self.tmp / "briefs" / "2026-09").mkdir(parents=True)
        (self.tmp / "tools").mkdir()
        shutil.copy(TOOLS / "sync-daily.py", self.tmp / "tools" / "sync-daily.py")
        (self.tmp / "index.html").write_text(
            '<section id="auto">\n  <h2 class="cat-title">🚗 汽车 <span class="count">0 篇</span></h2>\n'
            '  <div class="report-list">\n  </div>\n</section>\n'
            '<section id="daily">\n  <h2 class="cat-title">📰 每日简报 <span class="count">0 组 / 0 篇</span></h2>\n'
            '  <div class="report-list">\n  </div>\n</section>\n', encoding="utf-8")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def run_sync(self, *args):
        return subprocess.run([sys.executable, str(self.tmp / "tools" / "sync-daily.py"), *args],
                              cwd=self.tmp, capture_output=True, text=True)

    def brief(self, name: str) -> None:
        (self.tmp / name).write_text(
            f'<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">'
            f'<title>{name}</title></head><body>x</body></html>', encoding="utf-8")

    def test_stray_root_brief_is_relocated(self):
        self.brief("evolution-brief-2026-09-26.html")
        self.assertEqual(self.run_sync().returncode, 0)
        self.assertFalse((self.tmp / "evolution-brief-2026-09-26.html").exists())
        self.assertTrue((self.tmp / "briefs/2026-09/evolution-brief-2026-09-26.html").exists())

    def test_daily_is_regenerated_from_disk(self):
        (self.tmp / "briefs/2026-09/evolution-brief-2026-09-01.html").write_text(
            "<html><title>a</title></html>", encoding="utf-8")
        (self.tmp / "briefs/2026-09/evolution-brief-2026-09-02.html").write_text(
            "<html><title>b</title></html>", encoding="utf-8")
        self.run_sync()
        html = (self.tmp / "index.html").read_text(encoding="utf-8")
        self.assertIn("briefs/2026-09/evolution-brief-2026-09-01.html", html)
        self.assertIn("briefs/2026-09/evolution-brief-2026-09-02.html", html)
        self.assertIn("1 组 / 2 篇", html)   # 1 month group (no HN briefs)

    def test_new_month_creates_a_new_group(self):
        (self.tmp / "briefs" / "2026-10").mkdir()
        (self.tmp / "briefs/2026-10/evolution-brief-2026-10-01.html").write_text(
            "<html><title>c</title></html>", encoding="utf-8")
        self.run_sync()
        html = (self.tmp / "index.html").read_text(encoding="utf-8")
        self.assertIn("10月简报（1篇）", html)
        self.assertIn("1 组 / 1 篇", html)

    def test_check_reports_drift_without_writing(self):
        self.brief("evolution-brief-2026-09-26.html")
        r = self.run_sync("--check")
        self.assertEqual(r.returncode, 1)
        self.assertTrue((self.tmp / "evolution-brief-2026-09-26.html").exists(),
                        "--check must not move anything")

    def test_idempotent(self):
        self.brief("hn-brief-2026-09-26.html")
        self.run_sync()
        r = self.run_sync("--check")
        self.assertEqual(r.returncode, 0, r.stdout)
        self.brief("evolution-brief-2026-09-27.html")
        r = self.run_sync("--check")
        self.assertEqual(r.returncode, 1, "a new brief must be detected")

    def test_bad_count_badge_is_repaired(self):
        html = (self.tmp / "index.html").read_text(encoding="utf-8")
        html = html.replace('<span class="count">0 篇</span>', '<span class="count">99 篇</span>')
        html = html.replace("</div>\n</section>",
                            '<div class="report">x</div>\n</div>\n</section>', 1)
        (self.tmp / "index.html").write_text(html, encoding="utf-8")
        self.run_sync()
        out = (self.tmp / "index.html").read_text(encoding="utf-8")
        self.assertIn('<span class="count">1 篇</span>', out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
