"""
NumPy 02.1 - numpy 数据类型

常用 dtype：bool_ / int / uint / float / complex 等
"""
import numpy as np

# 布尔型
arr_bool = np.array([True, False, True], dtype=np.bool_)
print("bool_:", arr_bool, arr_bool.dtype)

# 整数型（有符号）
print("\n有符号整数:")
print("int8  范围 -128~127:", np.array([127], dtype=np.int8).dtype)
print("int16 范围 -32768~32767")
print("int32 范围 -2^31~2^31-1")
print("int64 范围 -2^63~2^63-1")

# 整数型（无符号）
print("\n无符号整数:")
print("uint8  范围 0~255:", np.array([255], dtype=np.uint8).dtype)
print("uint16 范围 0~65535")
print("uint32 范围 0~4294967295")
print("uint64 范围 0~2^64-1")

# int_ / intc / intp（平台相关）
print("\n平台相关:")
print("int_ 默认整数:", np.array([1]).dtype)
print("intp 索引用整数")

# 浮点型
print("\n浮点型:")
print("float_   float64 简写:", np.array([1.0]).dtype)
print("float16  半精度 1符号+5指数+10尾数位")
print("float32  单精度 1符号+8指数+23尾数位")
print("float64  双精度 1符号+11指数+52尾数位")

# 复数型
print("\n复数型:")
print("complex_  complex128 简写，128位复数")
print("complex64 双32位浮点(实部+虚部):", np.array([1+2j], dtype=np.complex64).dtype)
print("complex128 双64位浮点(实部+虚部):", np.array([1+2j]).dtype)
