"""
NumPy 03 - Routines 函数

常用签名：
  np.ones(shape, dtype=None, order='C')
  np.zeros(shape, dtype=float, order='C')
  np.full(shape, fill_value, dtype=None, order='C')
  np.eye(N, M=None, k=0, dtype=float)           # k: 对角线偏移，0为主对角线
  np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
  np.arange([start,] stop [,step,] dtype=None)
  np.random.randint(low, high=None, size=None, dtype='l')
  np.random.normal(loc=0, scale=1, size=None)   # 正态分布

用途详解：

  np.zeros 全 0 数组
    - 占位数组：预先分配内存再逐步填充
    - 累加器：result = np.zeros(n) 后循环 +=
    - 掩码/二值图：初始化后按条件赋值

  np.ones 全 1 数组
    - 神经网络权重初始化（常配合 scale）
    - 掩码：与目标数组相乘做筛选
    - 概率：均匀先验

  np.full 指定值填充
    - 批量设置常数：如填充 -1、NaN
    - 构建特殊矩阵（非 0/1 的对角线等）

  np.eye 单位矩阵
    - 线性代数：矩阵求逆、特征值分解
    - k 参数：上/下对角线，用于构造带状矩阵

  np.arange 等差整数序列
    - 循环索引：for i in np.arange(n)
    - 坐标轴刻度、网格生成
    - 注意：不包含 stop，步长可指定

  np.linspace 等分区间
    - 绘图横轴：x = np.linspace(0, 2*np.pi, 100) 画 sin
    - 插值采样：在 [a,b] 内均匀取 n 个点
    - endpoint=True 时包含右端点

  np.random.rand  [0,1) 均匀分布
    - 蒙特卡洛模拟、随机采样
    - 生成随机权重、dropout 掩码

  np.random.randint  随机整数
    - 随机抽样、打乱索引
    - 模拟掷骰子、抽奖

  np.random.normal  正态分布
    - 模拟测量误差、噪声
    - 股价/收益模拟、深度学习权重初始化

  np.sum/mean/std/min/max
    - 描述性统计：数据探索
    - 特征工程：构造均值、方差特征
    - 归一化：(x - mean) / std
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
print("np.random.normal(0, 1, 5) 正态分布:", np.random.normal(0, 1, 5))

print("\n=== 3. 数学 / 统计 routines ===")
arr = np.array([1, 2, 3, 4, 5])
print(f"arr = {arr}")
print("np.sum(arr):", np.sum(arr))
print("np.mean(arr):", np.mean(arr))
print("np.std(arr):", np.std(arr))
print("np.min(arr), np.max(arr):", np.min(arr), np.max(arr))
