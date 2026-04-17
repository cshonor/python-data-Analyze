# NumPy 学习笔记

NumPy 是 Python 科学计算的基础库，提供高性能的多维数组对象和数值计算工具。

## 目录结构

| 文件 | 说明 |
|------|------|
| 01_create_ndarray.py | 基础：数组创建 |
| 02.ndarray元素统一.py | 元素类型 |
| 02_numpy_data_types.py | 数据类型：float32/64 等 |
| 03_ndarray_indexing_slicing.py | 核心：索引与切片 |
| 04.ndarray读写.py | 读写、索引、切片 |
| 04_ndarray_shape_operations.py | reshape/flatten：形状操作 |
| 05_ndarray_basic_operations.md | 基本运算（加减乘除、点积等） |
| 06_concatenate_ndarrays.py | 数组拼接：concatenate |
| 07_split_ndarrays.md | 数组拆分：split |
| 08_broadcasting_mechanism.md | 广播机制 |
| 09_ndarray_aggregation_functions.md | 聚合函数：sum/mean/std 等 |
| 10_numpy_search_sort.md | 查找与排序：argsort/argmax 等 |
| 11_numpy_math_arithmetic_functions.md | 数学与算术函数：log/exp/where 等 |
| 12_ndarray_append_insert.md | append/insert（了解性能坑点） |
| 13_ndarray_delete_flatten_reshape.md | delete/flatten/reshape/flip |
| 14_numpy_routines.py | routines：随机数/矩阵生成等 |
| 15_numpy_routines_practice.py | routines 练习 |
| numpy查找排序.md | （旧名）已重命名为 10_numpy_search_sort.md |

## 量化实用优先级（推荐学习顺序）

1. `01_create_ndarray.py`
2. `02_numpy_data_types.py`、`02.ndarray元素统一.py`
3. `03_ndarray_indexing_slicing.py`、`04_ndarray_shape_operations.py`
4. `05_ndarray_basic_operations.md`、`08_broadcasting_mechanism.md`
5. `09_ndarray_aggregation_functions.md`、`11_numpy_math_arithmetic_functions.md`
6. `10_numpy_search_sort.md`（选股/因子排序常用）
7. `06_concatenate_ndarrays.py`、`07_split_ndarrays.md`
8. `12_ndarray_append_insert.md`、`13_ndarray_delete_flatten_reshape.md`（了解即可）

## 学习资源

- [NumPy 官方文档](https://numpy.org/doc/stable/)
- [NumPy 快速入门](https://numpy.org/doc/stable/user/quickstart.html)
