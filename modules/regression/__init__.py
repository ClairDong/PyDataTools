"""
线性回归模块
"""
import sys
import os

# 添加项目根目录到Python路径（如果还没有）
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from modules.regression.core import linear_regression_from_csv
from modules.regression.data_generator import generate_test_data
from modules.regression.plotter import plot_regression_results

__all__ = ['linear_regression_from_csv', 'generate_test_data', 'plot_regression_results']
