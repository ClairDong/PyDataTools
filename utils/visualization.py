"""
通用可视化工具
统一配置matplotlib的中文显示等设置
"""
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform
import os

# 全局变量：是否支持中文显示
CHINESE_FONT_AVAILABLE = False

def setup_chinese_font():
    """
    配置matplotlib支持中文显示
    自动检测系统可用的中文字体，如果找不到则使用备用方案
    """
    global CHINESE_FONT_AVAILABLE
    
    # 根据操作系统选择字体
    system = platform.system()
    
    if system == 'Windows':
        # Windows系统字体
        font_list = ['SimHei', 'Microsoft YaHei', 'KaiTi', 'FangSong', 'SimSun']
    elif system == 'Darwin':  # macOS
        # macOS系统字体
        font_list = ['Arial Unicode MS', 'PingFang SC', 'STHeiti', 'Heiti TC']
    else:
        # Linux系统字体（Streamlit Cloud使用Linux）
        # 尝试使用常见的Linux中文字体
        font_list = [
            'WenQuanYi Micro Hei',      # 文泉驿微米黑
            'WenQuanYi Zen Hei',         # 文泉驿正黑
            'Noto Sans CJK SC',         # Google Noto字体
            'Source Han Sans CN',        # 思源黑体
            'Droid Sans Fallback',      # Android字体
            'AR PL UMing CN',            # 文鼎字体
        ]
    
    # 查找系统中可用的字体
    available_fonts = [f.name for f in fm.fontManager.ttflist]
    
    # 找到第一个可用的字体
    selected_font = None
    for font in font_list:
        if font in available_fonts:
            selected_font = font
            CHINESE_FONT_AVAILABLE = True
            break
    
    if selected_font:
        plt.rcParams['font.sans-serif'] = [selected_font] + plt.rcParams['font.sans-serif']
    else:
        # 如果没有找到中文字体，使用DejaVu Sans
        # 这个字体不支持中文，但至少不会显示方块（会显示为空白或问号）
        plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
        CHINESE_FONT_AVAILABLE = False
    
    # 解决负号显示问题
    plt.rcParams['axes.unicode_minus'] = False

def get_label(label_cn, label_en):
    """
    根据字体支持情况返回合适的标签
    如果支持中文返回中文，否则返回英文
    """
    return label_cn if CHINESE_FONT_AVAILABLE else label_en

# 初始化时自动配置
setup_chinese_font()
