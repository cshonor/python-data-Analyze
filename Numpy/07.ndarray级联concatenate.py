"""
NumPy 07 - ndarray 级联 concatenate

ndarray 级联 = 把多个 numpy 数组按行 / 按列拼在一起，用函数：np.concatenate()

口诀：axis=0 上下拼（行增加），axis=1 左右拼（列增加）
"""
import numpy as np

print("=== 1. 按行拼接（竖着拼，axis=0）===")
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
c = np.concatenate([a, b], axis=0)
print("a:\n", a)
print("b:\n", b)
print("concatenate axis=0:\n", c)
# [[1 2]
#  [3 4]
#  [5 6]]

print("\n=== 2. 按列拼接（横着拼，axis=1）===")
a = np.array([[1], [2]])
b = np.array([[3], [4]])
c = np.concatenate([a, b], axis=1)
print("a:\n", a)
print("b:\n", b)
print("concatenate axis=1:\n", c)
# [[1 3]
#  [2 4]]
