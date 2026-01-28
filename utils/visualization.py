"""
通用可视化工具
统一配置matplotlib的中文显示等设置
"""
import matplotlib.pyplot as plt

def setup_chinese_font():
    """
    配置matplotlib支持中文显示
    """
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False

# 初始化时自动配置
setup_chinese_font()
