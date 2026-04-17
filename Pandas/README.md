# Pandas（量化方向）学习笔记

Pandas 在量化中主要负责：**行情/因子数据清洗**、**时间序列对齐**、**多标的结构化**、以及回测所需的数据准备。

## 目录结构

```text
Pandas/
├── README.md
├── 00_core_objects/
├── 01_core_data_operations/
├── 02_data_cleaning_preprocessing/
├── 03_time_series_for_quant/
├── 04_multi_asset_data_handling/
└── 05_quant_practice_cases/
```

## 量化常见坑（建议先记住）

- **未来函数**：信号生成与执行要错位，常用 `shift(1)` 做 T-1 生成、T 执行
- **时间对齐**：多数据源合并优先用 `merge_asof` 或统一到同一交易日索引
- **多标的数据结构**：推荐用 `MultiIndex (date, symbol)` 或宽表/长表转换配合 `stack/unstack`

## 学习资源

- [Pandas 官方文档](https://pandas.pydata.org/docs/)
- [Pandas 中文文档](https://www.pypandas.cn/)
