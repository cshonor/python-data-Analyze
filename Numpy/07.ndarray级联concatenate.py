"""
NumPy 07 - 1.5.1 ndarray 级联 (np.concatenate 完全解析)

np.concatenate 是 NumPy 中最核心的数组拼接函数，能将多个**形状兼容**的数组沿指定维度（轴）
合并为一个新数组，是数据预处理、矩阵操作中高频使用的工具。

函数格式：np.concatenate((a1, a2, ...), axis=0, out=None, dtype=None)
  参数 (a1, a2, ...)：必选，待拼接数组序列（必须是元组/列表形式）
  axis：可选，默认 0；二维中 0=行方向、1=列方向
  核心规则：除拼接轴外，其他维度形状必须完全一致

级联注意事项：
  - 级联的参数是列表：一定要加中括号 [a, b] 或 (a, b)
  - 维度必须相同，形状相符
  - 可通过 axis 参数改变级联方向
口诀：axis=0 上下拼（行增加），axis=1 左右拼（列增加）

简化函数：vstack=axis=0, hstack=axis=1, dstack=axis=2（3维深度拼接）
"""
import numpy as np

# 场景1：一维数组拼接（仅支持 axis=0）
print("=== 1. 一维数组拼接 ===")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
res1 = np.concatenate((arr1, arr2))  # axis=0 可省略
print("一维拼接结果：", res1)  # [1 2 3 4 5 6]

# 场景2：二维数组拼接（最常用）
print("\n=== 2. 二维数组拼接 ===")
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
arr4 = np.array([[7, 8, 9], [10, 11, 12]])
res2 = np.concatenate((arr3, arr4), axis=0)  # 沿行拼接，行数增加
print("沿行拼接 axis=0:\n", res2)
res3 = np.concatenate((arr3, arr4), axis=1)  # 沿列拼接，列数增加
print("沿列拼接 axis=1:\n", res3)

# 场景3：高维数组拼接（3维，axis=0 沿深度）
print("\n=== 3. 三维数组拼接 ===")
arr5 = np.arange(12).reshape(2, 2, 3)
arr6 = np.arange(12, 24).reshape(2, 2, 3)
res4 = np.concatenate((arr5, arr6), axis=0)
print("3维沿深度拼接形状：", res4.shape)  # (4, 2, 3)

# 场景4：形状不兼容报错
print("\n=== 4. 常见错误：形状不兼容 ===")
arr7 = np.array([[1, 2]])  # 1行2列，与 arr3(2行3列) 列数不一致
try:
    np.concatenate((arr3, arr7), axis=0)
except ValueError as e:
    print("报错信息：", e)

# 场景5：vstack / hstack 与 concatenate 等价
print("\n=== 5. vstack / hstack 简化版 ===")
# vstack = concatenate axis=0，hstack = concatenate axis=1
print("vstack 等价 axis=0:", np.array_equal(res2, np.vstack((arr3, arr4))))
print("hstack 等价 axis=1:", np.array_equal(res3, np.hstack((arr3, arr4))))
