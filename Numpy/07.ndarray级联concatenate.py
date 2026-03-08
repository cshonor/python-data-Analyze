"""
NumPy 07 - 1.5.1 ndarray 级联

ndarray 级联 = 把多个 numpy 数组按行 / 按列拼在一起

级联的注意事项：
  - 级联的参数是列表：一定要加中括号 [a, b] 或 (a, b)
  - 维度必须相同
  - 形状相符（沿 axis 方向外的维度需一致）
  - 级联的方向默认是 shape 这个 tuple 的第一个值所代表的维度方向
  - 可通过 axis 参数改变级联的方向

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

print("\n=== 3. np.hstack 与 np.vstack ===")
# np.vstack = concatenate axis=0，np.hstack = concatenate axis=1
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
print("vstack（竖向）:\n", np.vstack([x, y]))
print("hstack（横向）:\n", np.hstack([x, y]))
