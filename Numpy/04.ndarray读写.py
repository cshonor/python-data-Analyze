"""
NumPy 04 - ndarray 读写

NumPy 支持将数组保存到文件、从文件加载。
常用：.npy（二进制）/ .npz（压缩）/ .txt .csv（文本）
"""
import numpy as np
import os

# 创建示例数组
arr = np.array([[1, 2, 3], [4, 5, 6]])

print("=== 1. 二进制格式 .npy（推荐，保留 dtype 等完整信息）===")
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
