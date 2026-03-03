"""
NumPy 02 - ndarray 元素统一

ndarray 要求所有元素必须是同一种数据类型（dtype）。
若传入混合类型，NumPy 会自动提升为更“宽”的类型以保持统一。
"""
import numpy as np

print("=== 元素类型自动统一 ===")

# 1. 纯整数 → int
arr1 = np.array([1, 2, 3])
print(f"[1,2,3] dtype: {arr1.dtype}")  # int64 或 int32

# 2. 整数 + 浮点数 → 自动提升为 float
arr2 = np.array([1, 2, 3.0])
print(f"[1,2,3.0] dtype: {arr2.dtype}")  # float64

# 3. 整数 + 字符串 → 统一为字符串
arr3 = np.array([1, 2, "a"])
print(f"[1,2,'a'] dtype: {arr3.dtype}")  # <U11 或 str

# 4. 手动指定 dtype
arr4 = np.array([1, 2, 3], dtype=float)
print(f"指定 dtype=float: {arr4} dtype: {arr4.dtype}")

arr5 = np.array([1.1, 2.2, 3.3], dtype=int)  # 浮点会被截断
print(f"指定 dtype=int: {arr5} dtype: {arr5.dtype}")  # [1 2 3]
