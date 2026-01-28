"""
线性回归数据生成模块
"""
import numpy as np
import pandas as pd


def generate_test_data(n_samples=100, noise=10, random_state=42, output_file='data.csv'):
    """
    生成一组随机的测试数据（X, Y）并保存为CSV文件
    
    参数:
        n_samples: 样本数量，默认100
        noise: 噪声水平，默认10
        random_state: 随机种子，默认42（保证结果可重现）
        output_file: 输出CSV文件名，默认'data.csv'
    
    返回:
        csv_file: 保存的CSV文件路径
    """
    np.random.seed(random_state)
    
    # 生成X数据（0到100之间的随机数）
    X = np.random.uniform(0, 100, n_samples)
    
    # 生成Y数据：Y = 2*X + 30 + 噪声
    # 这是一个线性关系，斜率为2，截距为30
    true_slope = 2
    true_intercept = 30
    Y = true_slope * X + true_intercept + np.random.normal(0, noise, n_samples)
    
    # 创建DataFrame
    df = pd.DataFrame({
        'X': X,
        'Y': Y
    })
    
    # 保存为CSV文件
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"数据已成功保存到: {output_file}")
    print(f"样本数量: {len(df)}")
    
    return output_file


if __name__ == "__main__":
    # 生成测试数据并保存为CSV
    csv_file = generate_test_data(n_samples=100, noise=10, output_file='data.csv')
    print(f"\nCSV文件 '{csv_file}' 已创建完成！")
