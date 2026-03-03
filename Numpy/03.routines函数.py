"""
NumPy 03 - Routines 函数

NumPy 提供了大量 routines（例程函数），用于数组创建、操作、计算等。
官方分类：Array creation / Array manipulation / Mathematical / Linear algebra / Random 等。
"""
import numpy as np

print("=== 1. 数组创建类 routines ===")
print("np.zeros(3):", np.zeros(3))
print("np.ones((2, 3)):\n", np.ones((2, 3)))
print("np.full((2, 2), 7):", np.full((2, 2), 7))
print("np.eye(3) 单位矩阵:\n", np.eye(3))
print("np.arange(0, 10, 2):", np.arange(0, 10, 2))
print("np.linspace(0, 1, 5):", np.linspace(0, 1, 5))

print("\n=== 2. 随机数 routines ===")
np.random.seed(42)
print("np.random.rand(2, 3):\n", np.random.rand(2, 3))
print("np.random.randint(1, 10, size=5):", np.random.randint(1, 10, size=5))

print("\n=== 3. 数学 / 统计 routines ===")
arr = np.array([1, 2, 3, 4, 5])
print(f"arr = {arr}")
print("np.sum(arr):", np.sum(arr))
print("np.mean(arr):", np.mean(arr))
print("np.std(arr):", np.std(arr))
print("np.min(arr), np.max(arr):", np.min(arr), np.max(arr))
