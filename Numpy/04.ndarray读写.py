"""
NumPy 04 - ndarray 读写

1.4.2 列表/ndarray 访问：类似 Python list，arr[1] 取第 2 行
  l2 = [[1,2,3],[2,3,4]]  →  l2[1] = [2,3,4]
  arr = np.array(l2)       →  arr[1] = array([2,3,4])

文件读写：.npy（二进制）/ .npz（压缩）/ .txt .csv（文本）
"""
import numpy as np
import os

# 列表/ndarray 访问：正索引、负索引、嵌套
l1 = [1, 2, 3, 4, 5]
print("l1[1]:", l1[1])      # 2
print("l1[-1]:", l1[-1])    # 5 负索引取最后

# 1D ndarray：直接索引、变量索引
np.random.seed(42)
arr1 = np.random.randint(0, 100, size=10)
print("arr1:", arr1)
print("arr1[1], arr1[2]:", arr1[1], arr1[2])  # 直接索引
index = 1
print("arr1[index]:", arr1[index])  # 变量索引

l2 = [[1, 2, 3], [2, 3, 4]]
arr = np.array(l2)
print("l2[1]:", l2[1])      # [2, 3, 4]
print("l2[1][0]:", l2[1][0])  # 2 嵌套访问
print("arr[1]:", arr[1])    # array([2, 3, 4])
# ndarray的高维数组访问，使用 [dim1_index, dim2_index, ...]
print("arr[1,0]:", arr[1, 0])  # 2

print("\n=== 1. 二进制格式 .npy（推荐，保留 dtype 等完整信息）===")
np.save("temp_array.npy", arr)
loaded = np.load("temp_array.npy")
print("保存后读取:", loaded)
os.remove("temp_array.npy")  # 清理临时文件

print("\n=== 2. 文本格式 .txt / .csv ===")
np.savetxt("temp_data.txt", arr, fmt="%d")
loaded_txt = np.loadtxt("temp_data.txt")
print("savetxt 保存后 loadtxt 读取:\n", loaded_txt)
os.remove("temp_data.txt")

print("\n=== 3. CSV 格式（指定分隔符）===")
np.savetxt("temp_data.csv", arr, delimiter=",", fmt="%d")
loaded_csv = np.loadtxt("temp_data.csv", delimiter=",")
print("CSV 读取:\n", loaded_csv)
os.remove("temp_data.csv")
