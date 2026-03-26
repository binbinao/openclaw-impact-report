"""
生成报告图片
"""

from PIL import Image, ImageDraw, ImageFont
import os

# 字体路径
FONT_PATHS = {
    'bold': '/usr/share/fonts/google-noto-cjk/NotoSansCJKsc-Bold.otf',
    'medium': '/usr/share/fonts/google-noto-cjk/NotoSansCJKsc-Medium.otf',
    'regular': '/usr/share/fonts/google-noto-cjk/NotoSansCJKsc-Regular.otf',
}

def create_future_trends_image(output_path: str):
    """创建AI研究未来趋势图片"""
    width, height = 1200, 800
    
    # 创建画布 - 深色背景
    img = Image.new('RGB', (width, height), color='#0f172a')
    draw = ImageDraw.Draw(img)
    
    # 渐变背景
    for y in range(height):
        r = int(15 + (y / height) * 10)
        g = int(23 + (y / height) * 20)
        b = int(42 + (y / height) * 30)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # 加载字体
    title_font = ImageFont.truetype(FONT_PATHS['bold'], 48)
    subtitle_font = ImageFont.truetype(FONT_PATHS['medium'], 28)
    text_font = ImageFont.truetype(FONT_PATHS['regular'], 22)
    
    # 标题
    title = "🎯 AI研究未来趋势"
    bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = bbox[2] - bbox[0]
    draw.text(((width - title_width) // 2, 40), title, fill='#10b981', font=title_font)
    
    # 三个阶段
    stages = [
        {
            'title': '短期趋势 (1-2年)',
            'color': '#34d399',
            'items': [
                '• AI研究助手普及',
                '• 自动化实验增加',
                '• 论文辅助撰写',
                '• 评审系统智能化'
            ]
        },
        {
            'title': '中期趋势 (3-5年)',
            'color': '#fbbf24',
            'items': [
                '• AI主导研究',
                '• 跨领域研究加速',
                '• 研究民主化',
                '• 新研究范式'
            ]
        },
        {
            'title': '长期趋势 (5年以上)',
            'color': '#f87171',
            'items': [
                '• AGI研究',
                '• 科学发现加速',
                '• 研究伦理重构',
                '• 突破人类认知极限'
            ]
        }
    ]
    
    # 绘制三个阶段
    x_positions = [80, 440, 800]
    
    for i, stage in enumerate(stages):
        x = x_positions[i]
        
        # 阶段标题背景
        draw.rounded_rectangle(
            [(x, 120), (x + 320, 170)],
            radius=8,
            fill=stage['color']
        )
        
        # 阶段标题文字
        bbox = draw.textbbox((0, 0), stage['title'], font=subtitle_font)
        title_w = bbox[2] - bbox[0]
        draw.text((x + (320 - title_w) // 2, 130), stage['title'], fill='#0f172a', font=subtitle_font)
        
        # 内容项
        y = 200
        for item in stage['items']:
            draw.text((x + 20, y), item, fill='#e2e8f0', font=text_font)
            y += 45
        
        # 连接箭头（除了最后一个）
        if i < 2:
            arrow_x = x + 340
            arrow_y = 350
            draw.polygon(
                [(arrow_x, arrow_y), (arrow_x + 30, arrow_y - 15), (arrow_x + 30, arrow_y + 15)],
                fill='#6366f1'
            )
    
    # 底部说明
    footer = "从AI辅助到AI主导，研究范式正在根本性转变"
    bbox = draw.textbbox((0, 0), footer, font=text_font)
    footer_width = bbox[2] - bbox[0]
    draw.text(((width - footer_width) // 2, 700), footer, fill='#94a3b8', font=text_font)
    
    # 保存
    img.save(output_path)
    print(f"✅ 已生成: {output_path}")
    return output_path


def create_challenges_image(output_path: str):
    """创建挑战与风险图片"""
    width, height = 1200, 700
    
    # 创建画布 - 深色背景
    img = Image.new('RGB', (width, height), color='#0f172a')
    draw = ImageDraw.Draw(img)
    
    # 渐变背景
    for y in range(height):
        r = int(15 + (y / height) * 15)
        g = int(23 + (y / height) * 10)
        b = int(42 + (y / height) * 20)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # 加载字体
    title_font = ImageFont.truetype(FONT_PATHS['bold'], 48)
    subtitle_font = ImageFont.truetype(FONT_PATHS['medium'], 28)
    text_font = ImageFont.truetype(FONT_PATHS['regular'], 22)
    
    # 标题
    title = "⚠️ 挑战与风险"
    bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = bbox[2] - bbox[0]
    draw.text(((width - title_width) // 2, 40), title, fill='#ef4444', font=title_font)
    
    # 三个类别
    categories = [
        {
            'title': '技术挑战',
            'color': '#f87171',
            'items': [
                '• 想法质量',
                '• 实验可靠性',
                '• 结果解读',
                '• 幻觉问题'
            ]
        },
        {
            'title': '伦理风险',
            'color': '#fbbf24',
            'items': [
                '• 同行评审压力',
                '• 学术诚信',
                '• 知识产权',
                '• 就业影响'
            ]
        },
        {
            'title': '应对建议',
            'color': '#34d399',
            'items': [
                '• 建立标准',
                '• 人机协作',
                '• 伦理培训',
                '• 技术保障'
            ]
        }
    ]
    
    # 绘制三个类别
    x_positions = [80, 440, 800]
    
    for i, cat in enumerate(categories):
        x = x_positions[i]
        
        # 类别标题背景
        draw.rounded_rectangle(
            [(x, 120), (x + 320, 170)],
            radius=8,
            fill=cat['color']
        )
        
        # 类别标题文字
        bbox = draw.textbbox((0, 0), cat['title'], font=subtitle_font)
        title_w = bbox[2] - bbox[0]
        draw.text((x + (320 - title_w) // 2, 130), cat['title'], fill='#0f172a', font=subtitle_font)
        
        # 内容项
        y = 200
        for item in cat['items']:
            draw.text((x + 20, y), item, fill='#e2e8f0', font=text_font)
            y += 45
    
    # 底部说明
    footer = "在拥抱变革的同时，需要审慎应对潜在风险"
    bbox = draw.textbbox((0, 0), footer, font=text_font)
    footer_width = bbox[2] - bbox[0]
    draw.text(((width - footer_width) // 2, 600), footer, fill='#94a3b8', font=text_font)
    
    # 保存
    img.save(output_path)
    print(f"✅ 已生成: {output_path}")
    return output_path


if __name__ == '__main__':
    output_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(output_dir, 'images')
    os.makedirs(images_dir, exist_ok=True)
    
    create_future_trends_image(os.path.join(images_dir, 'future_trends.png'))
    create_challenges_image(os.path.join(images_dir, 'challenges.png'))
    
    print("\n✅ 所有图片已生成！")