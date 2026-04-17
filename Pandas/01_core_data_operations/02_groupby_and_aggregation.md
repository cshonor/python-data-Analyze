# 数据聚合与索引操作

> 覆盖：43-pandas聚合操作 → 48-stack和unstack操作

## 一、pandas 聚合操作

- 核心聚合函数：`sum()` / `mean()` / `count()` / `min()` / `max()` / `std()`
- 聚合方向：`axis=0`（列聚合）/ `axis=1`（行聚合）
- 自定义聚合：`df.agg(func)` 支持传入多个函数或字典
- 与 `groupby` 结合：分组后聚合是数据分析核心场景

## 二、pandas 对象习题讲解

- 典型题型：基础运算与缺失值、数据筛选与索引、简单聚合统计
- 解题思路：先理解需求 → 选择合适方法 → 验证结果

## 三、pandas 单层索引

- 单层索引类型：`pd.Index`（默认）、`pd.RangeIndex`（连续整数）
- 索引操作：
  - 重命名：`df.rename(index={...}, columns={...})`
  - 重置索引：`df.reset_index(drop=True)`（将索引转为列）
  - 设置索引：`df.set_index('col')`（将列转为索引）
- 索引唯一性：`index.is_unique` 检查是否重复

## 四、pandas 多层索引

- 多层索引（MultiIndex）：行/列支持多级标签，适合分层数据
- 构造方式：
  - 从元组列表创建：`pd.MultiIndex.from_tuples([...])`
  - 从笛卡尔积创建：`pd.MultiIndex.from_product([level1, level2])`
- 层级命名：`index.names = ['level1', 'level2']`

## 五、多层索引的访问

- 按层级访问：`df.loc[('level1_val', 'level2_val'), :]`
- 跨层级筛选：`df.xs('val', level='level_name')`
- 列多层索引：与行索引访问逻辑一致

## 六、stack 和 unstack 操作

- `stack()`：将列索引转为行索引（宽表转长表）
- `unstack()`：将行索引转为列索引（长表转宽表）
- 核心作用：重塑数据形状，适配不同分析场景
