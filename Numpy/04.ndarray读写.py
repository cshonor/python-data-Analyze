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
# fancy indexing：用整数列表作为索引，按顺序、可重复取元素
index1 = [1, 2, 1, 2, 1, 2]
print("arr1[index1]:", arr1[index1])

l2 = [[1, 2, 3], [2, 3, 4]]
arr = np.array(l2)
print("l2[1]:", l2[1])      # [2, 3, 4]
print("l2[1][0]:", l2[1][0])  # 2 嵌套访问
print("arr[1]:", arr[1])    # array([2, 3, 4])
# ndarray的高维数组访问，使用 [dim1_index, dim2_index, ...]
print("arr[1,0]:", arr[1, 0])  # 2

# 1.4.3 切片访问
print("\n=== 1.4.3 切片访问 ===")
perm = np.random.permutation(10)
print("np.random.permutation(10):", perm)#生成10个随机整数
# 切片 [start:stop:step]，与 Python list 一致
print("perm[2:5]:", perm[2:5])   # 索引 2 到 4
print("perm[::2]:", perm[::2])   # 步长 2
print("perm[::-1]:", perm[::-1]) # 反转
# 在原始数据中，随机取3个数
rand_indices = np.random.permutation(10)[[0, 1, 2]]  # 或 [:3] 这行代码的作用是生成 0-9 的随机乱序数组，然后取前 3 个元素
#[[0, 1, 2]]：这是双层中括号，表示取前 3 个元素。
#这是 NumPy 的花式索引（Fancy Indexing），表示从前面的乱序数组中，取出索引为 0、1、2 的元素（也就是前 3 个元素）。
#注意：这里用双层中括号 [[0,1,2]] 和单层 [0,1,2] 效果一致，都是取这三个索引的元素，返回一维数组。
print("随机3个索引:", rand_indices)
print("arr1中对应值:", arr1[rand_indices])

print("\n=== 1. 二进制格式 .npy（推荐，保留 dtype 等完整信息）===")
np.save("temp_array.npy", arr)#将数组保存为二进制文件，文件名是temp_array.npy np.save() 是 NumPy 库中用于将数组保存到二进制文件（.npy 格式）的核心函数
loaded = np.load("temp_array.npy")#从二进制文件中加载数组，文件名是temp_array.npy
print("保存后读取:", loaded)
os.remove("temp_array.npy")  # 清理文件

print("\n=== 2. 文本格式 .txt / .csv ===")
np.savetxt("temp_data.txt", arr, fmt="%d")#将数组保存为文本文件，文件名是temp_data.txt
loaded_txt = np.loadtxt("temp_data.txt")#从文本文件中加载数组，文件名是temp_data.txt
print("savetxt 保存后 loadtxt 读取:\n", loaded_txt)
os.remove("temp_data.txt")

print("\n=== 3. CSV 格式（指定分隔符）===")
np.savetxt("temp_data.csv", arr, delimiter=",", fmt="%d")#将数组保存为CSV文件，文件名是temp_data.csv
loaded_csv = np.loadtxt("temp_data.csv", delimiter=",")#从CSV文件中加载数组，文件名是temp_data.csv
print("CSV 读取:\n", loaded_csv)
os.remove("temp_data.csv")
