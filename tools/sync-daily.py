#!/usr/bin/env python3
"""Normalize the report site layout.

Idempotent. Safe to run any number of times, from anywhere in the repo.

What it fixes (the two failures the daily-brief generator makes):

1. Stray briefs written to the repo root instead of ``briefs/<YYYY-MM>/``.
   They are moved to the correct month directory.
2. The ``#daily`` section of ``index.html`` not listing a brief that exists on
   disk. The whole section is regenerated from the filesystem, so the month
   groups, their labels, and the badge can never drift again.

It also repairs a section ``count`` badge that disagrees with the number of
``.report`` cards in that section.

Usage:
    python3 tools/sync-daily.py          # apply changes
    python3 tools/sync-daily.py --check  # exit 1 if anything would change

Exit status: 0 = clean or fixed, 1 = --check found drift, 2 = error.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

BRIEF_RE = re.compile(r"^(evolution|hn)-brief-(\d{4})-(\d{2})-(\d{2})\.html$")
DIM = "\x1b[2m"
RED = "\x1b[31m"
GREEN = "\x1b[32m"
YELLOW = "\x1b[33m"
RESET = "\x1b[0m"


def repo_root(start: Path) -> Path:
    for d in [start.resolve(), *start.resolve().parents]:
        if (d / "index.html").is_file() and (d / "briefs").is_dir():
            return d
    raise SystemExit(f"{RED}error:{RESET} not inside the report repo")


def find_stray_briefs(root: Path) -> list[tuple[Path, Path]]:
    """Briefs sitting at the repo root that belong in briefs/<YYYY-MM>/."""
    out: list[tuple[Path, Path]] = []
    for f in sorted(root.iterdir()):
        if not f.is_file():
            continue
        m = BRIEF_RE.match(f.name)
        if not m:
            continue
        _, year, month, _day = m.groups()
        dest = root / "briefs" / f"{year}-{month}" / f.name
        if not dest.exists():
            out.append((f, dest))
    return out


def scan_briefs(root: Path) -> dict[str, dict[str, list[tuple[str, str]]]]:
    """{month: {'evolution': [(date, filename)], 'hn': [...]}} sorted ascending."""
    months: dict[str, dict[str, list[tuple[str, str]]]] = {}
    for d in sorted((root / "briefs").iterdir()):
        if not d.is_dir():
            continue
        bucket: dict[str, list[tuple[str, str]]] = {"evolution": [], "hn": []}
        for f in sorted(d.glob("*.html")):
            m = BRIEF_RE.match(f.name)
            if not m:
                continue
            kind, year, month, day = m.groups()
            key = "hn" if kind == "hn" else "evolution"
            bucket[key].append((f"{year}-{month}-{day}", f.name))
        months[d.name] = bucket
    return months


def date_links(month: str, entries: list[tuple[str, str]]) -> str:
    """Newest-first, ' · '-joined date links (existing index convention)."""
    ordered = sorted(entries, reverse=True)
    return " · ".join(
        f'<a href="briefs/{month}/{name}" style="font-size:12px;">{date[5:]}</a>'
        for date, name in ordered
    )


def card(icon: str, label: str, body: str, date: str) -> str:
    return (
        f'    <div class="report">\n'
        f'      <span class="icon">{icon}</span>\n'
        f'      <div class="info">\n'
        f'        <span style="color:var(--gray-500);font-size:13px;">{label}</span>\n'
        f'        <div class="desc">\n'
        f'          {body}\n'
        f'        </div>\n'
        f'      </div>\n'
        f'      <span class="date">{date}</span>\n'
        f'    </div>'
    )


def build_daily_section(months: dict[str, dict[str, list[tuple[str, str]]]]) -> str:
    cards: list[str] = []
    hn_all: list[tuple[str, str, str]] = []
    for month, bucket in months.items():
        for date, name in bucket["hn"]:
            hn_all.append((date, month, name))

    if hn_all:
        newest = max(d for d, _, _ in hn_all)[5:]
        links = " · ".join(
            f'<a href="briefs/{month}/{name}" style="font-size:12px;">{date[5:]}</a>'
            for date, month, name in sorted(hn_all, reverse=True)
        )
        cards.append(card("🗞️", f"Hacker News 日报（{len(hn_all)} 篇）", links, newest))

    groups = len(cards)
    total = len(hn_all)
    for month, bucket in sorted(months.items(), reverse=True):
        if not bucket["evolution"]:
            continue
        short = month[5:]
        cards.append(
            card(
                "📁",
                f"{short}月简报（{len(bucket['evolution'])}篇）",
                date_links(month, bucket["evolution"]),
                f"{short}月",
            )
        )
        groups += 1
        total += len(bucket["evolution"])

    body = "\n".join(cards)
    return (
        f'<section id="daily">\n'
        f'  <h2 class="cat-title">📰 每日简报 <span class="count">{groups} 组 / {total} 篇</span></h2>\n'
        f'  <div class="report-list">\n{body}\n  </div>\n</section>'
    )


def fix_count_badges(html: str) -> tuple[str, list[str]]:
    """Make each non-daily section badge equal its .report card count."""
    notes: list[str] = []
    for chunk in re.split(r'(?=<section id=")', html)[1:]:
        if not chunk.startswith('<section id="'):
            continue
        sid = chunk[len('<section id="'):].split('"', 1)[0]
        if sid == "daily":
            continue
        body = chunk.split("</section>", 1)[0]
        actual = body.count('class="report"')
        pat = re.compile(
            r'(<section id="' + re.escape(sid) + r'">.*?<span class="count">)(\d+)( 篇)',
            re.S,
        )
        m = pat.search(html)
        if m and int(m.group(2)) != actual:
            notes.append(f"{sid}: badge {m.group(2)} -> {actual}")
            html = html[: m.start(2)] + str(actual) + html[m.end(2):]
    return html, notes


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="report drift without writing")
    args = ap.parse_args()

    root = repo_root(Path.cwd())
    changed = False

    # 1. relocate stray root briefs
    stray = find_stray_briefs(root)
    for src, dest in stray:
        changed = True
        rel = dest.relative_to(root)
        print(f"{YELLOW}move{RESET}  {src.name} -> {rel}")
        if not args.check:
            dest.parent.mkdir(parents=True, exist_ok=True)
            src.rename(dest)

    # 2. regenerate #daily from the filesystem. In --check mode the strays are
    #    still at the root, so count the planned destinations too.
    idx_path = root / "index.html"
    html = idx_path.read_text(encoding="utf-8")
    months = scan_briefs(root)
    if args.check:
        for _src, dest in stray:
            m = BRIEF_RE.match(dest.name)
            kind, year, month, day = m.groups()
            key = "hn" if kind == "hn" else "evolution"
            months.setdefault(dest.parent.name, {"evolution": [], "hn": []})
            months[dest.parent.name][key].append((f"{year}-{month}-{day}", dest.name))
    section = build_daily_section(months)
    new_html, n = re.subn(
        r'<section id="daily">.*?</section>', lambda _: section, html, count=1, flags=re.S
    )
    if n == 0:
        print(f"{RED}error:{RESET} no <section id=\"daily\"> found in index.html", file=sys.stderr)
        return 2
    if new_html != html:
        changed = True
        old_badge = re.search(r'<section id="daily">.*?<span class="count">(.*?)<', html, re.S)
        new_badge = re.search(r'<span class="count">(.*?)<', section)
        print(
            f"{YELLOW}daily{RESET} badge "
            f"{(old_badge.group(1) if old_badge else '?')} -> "
            f"{(new_badge.group(1) if new_badge else '?')}"
        )
        html = new_html

    # 3. repair stale count badges
    html, notes = fix_count_badges(html)
    for note in notes:
        changed = True
        print(f"{YELLOW}badge{RESET} {note}")

    if changed:
        if not args.check:
            idx_path.write_text(html, encoding="utf-8")
        else:
            print(f"{RED}drift detected{RESET} (run without --check to fix)")
            return 1
        print(f"{GREEN}fixed{RESET}  index.html updated")
    else:
        print(f"{GREEN}ok{RESET}     layout and #daily already in sync")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
