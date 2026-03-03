"""
NumPy 01 - 创建 ndarray
"""
import numpy as np

#ndarray（N-dimensional array）即N 维数组，是 NumPy 库的核心数据结构，专门用于高效存储和操作同类型的数值数据（比如整数、浮点数）。
#可以把它理解为：
#1 维 ndarray = 普通的一维数组 / 列表（但性能远优于 Python 原生列表）
#2 维 ndarray = 表格 / 矩阵（行 + 列）
#3 维 ndarray = 立方体（行 + 列 + 深度）
#N 维 ndarray = 更高维度的数值集合

# 1. 创建数组
print("=== 创建数组 ===")
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr3 = np.zeros((3, 3))
arr4 = np.ones((2, 4))
arr5 = np.arange(0, 10, 2)
arr6 = np.linspace(0, 1, 5)

print(f"一维数组: {arr1}")
print(f"类型验证 type(arr1): {type(arr1)}")  # numpy.ndarray
print(f"二维数组:\n{arr2}")
print(f"零矩阵:\n{arr3}")
print(f"全1矩阵:\n{arr4}")
print(f"等差数列 arange(0,10,2): {arr5}")
print(f"线性间隔 linspace(0,1,5): {arr6}")

# 2. 数组属性
print("\n=== 数组属性 ===")
print(f"shape 形状: {arr2.shape}")
print(f"ndim 维度: {arr2.ndim}")
print(f"size 元素个数: {arr2.size}")
print(f"dtype 数据类型: {arr2.dtype}")
