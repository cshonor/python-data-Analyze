# Pandas（量化方向）学习笔记

Pandas 在量化中主要负责：**行情/因子数据清洗**、**时间序列对齐**、**多标的结构化**、以及回测所需的数据准备。

## 目录结构

```text
Pandas/
├── 00-基础核心对象/                # Series / DataFrame 基础
├── 01-核心数据操作/                # 索引筛选、聚合分组、合并连接、重塑透视
├── 02-数据清洗与预处理/            # 缺失值/异常值/重复值/复权与行情清洗
├── 03-时间序列与量化核心/          # DatetimeIndex、resample、rolling、shift(防未来函数)
├── 04-可视化基础/                  # Matplotlib 与 pandas 集成绘图
└── 05-量化实战案例/                # 策略/信号/绩效分析案例
```

## 量化常见坑（建议先记住）

- **未来函数**：信号生成与执行要错位，常用 `shift(1)` 做 T-1 生成、T 执行
- **时间对齐**：多数据源合并优先用 `merge_asof` 或统一到同一交易日索引
- **多标的数据结构**：推荐用 `MultiIndex (date, symbol)` 或宽表/长表转换配合 `stack/unstack`

## 学习资源

- [Pandas 官方文档](https://pandas.pydata.org/docs/)
- [Pandas 中文文档](https://www.pypandas.cn/)
