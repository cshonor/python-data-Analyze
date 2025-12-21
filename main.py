import numpy as np

def main():
    """NumPy基础示例"""
    
    # 1. 创建数组
    print("=== 创建数组 ===")
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    arr3 = np.zeros((3, 3))
    arr4 = np.ones((2, 4))
    arr5 = np.arange(0, 10, 2)
    arr6 = np.linspace(0, 1, 5)
    
    print(f"一维数组: {arr1}")
    print(f"二维数组:\n{arr2}")
    print(f"零矩阵:\n{arr3}")
    print(f"全1矩阵:\n{arr4}")
    print(f"等差数列: {arr5}")
    print(f"线性间隔: {arr6}")
    
    # 2. 数组属性
    print("\n=== 数组属性 ===")
    print(f"数组形状: {arr2.shape}")
    print(f"数组维度: {arr2.ndim}")
    print(f"数组大小: {arr2.size}")
    print(f"数据类型: {arr2.dtype}")
    
    # 3. 数组运算
    print("\n=== 数组运算 ===")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print(f"数组相加: {a + b}")
    print(f"数组相乘: {a * b}")
    print(f"点积: {np.dot(a, b)}")
    print(f"数组平方: {a ** 2}")
    
    # 4. 数组索引和切片
    print("\n=== 数组索引和切片 ===")
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(f"原数组:\n{arr}")
    print(f"第一行: {arr[0]}")
    print(f"第一列: {arr[:, 0]}")
    print(f"子数组:\n{arr[1:3, 1:3]}")
    
    # 5. 数组形状操作
    print("\n=== 数组形状操作 ===")
    arr_flat = np.array([1, 2, 3, 4, 5, 6])
    arr_reshaped = arr_flat.reshape(2, 3)
    print(f"原数组: {arr_flat}")
    print(f"重塑后:\n{arr_reshaped}")
    print(f"展平: {arr_reshaped.flatten()}")
    
    # 6. 数学函数
    print("\n=== 数学函数 ===")
    arr = np.array([1, 4, 9, 16, 25])
    print(f"原数组: {arr}")
    print(f"平方根: {np.sqrt(arr)}")
    print(f"正弦值: {np.sin(np.array([0, np.pi/2, np.pi]))}")
    print(f"指数: {np.exp([1, 2, 3])}")
    print(f"对数: {np.log([1, 10, 100])}")
    
    # 7. 统计函数
    print("\n=== 统计函数 ===")
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"数组: {arr}")
    print(f"平均值: {np.mean(arr)}")
    print(f"中位数: {np.median(arr)}")
    print(f"标准差: {np.std(arr)}")
    print(f"最大值: {np.max(arr)}")
    print(f"最小值: {np.min(arr)}")
    print(f"总和: {np.sum(arr)}")
    
    # 8. 随机数
    print("\n=== 随机数 ===")
    np.random.seed(42)  # 设置随机种子以便结果可复现
    random_arr = np.random.rand(3, 3)
    random_int = np.random.randint(1, 10, size=(2, 3))
    print(f"随机浮点数矩阵:\n{random_arr}")
    print(f"随机整数矩阵:\n{random_int}")
    
    # 9. 矩阵运算
    print("\n=== 矩阵运算 ===")
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    print(f"矩阵1:\n{matrix1}")
    print(f"矩阵2:\n{matrix2}")
    print(f"矩阵乘法:\n{np.dot(matrix1, matrix2)}")
    print(f"矩阵转置:\n{matrix1.T}")
    print(f"矩阵行列式: {np.linalg.det(matrix1)}")
    print(f"矩阵逆:\n{np.linalg.inv(matrix1)}")

if __name__ == "__main__":
    main()

