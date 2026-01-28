"""
线性回归模块
"""
from modules.regression.core import linear_regression_from_csv
from modules.regression.data_generator import generate_test_data
from modules.regression.plotter import plot_regression_results

__all__ = ['linear_regression_from_csv', 'generate_test_data', 'plot_regression_results']
