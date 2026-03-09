# 数据合并与高级变换

> 覆盖：63-replace替换 → 70-交叉表和透视表

## 一、replace 替换

- 单值替换：`df['col'].replace(old_val, new_val)`
- 多值/字典映射：`df['col'].replace([...], [...])` / `replace({...})`
- 正则替换：`replace(regex=r'^a', value='A')`

## 二、map 处理精确匹配与模糊匹配

- 精确匹配：`df['col'].map({key1: val1, ...})`
- 模糊匹配：结合 `str.contains()` 或正则

## 三、pandas 级联

- 核心函数：`pd.concat([df1, df2], axis=0/1)`
- 行级联 `axis=0` / 列级联 `axis=1`
- 参数：`ignore_index=True` / `join='inner'`

## 四、合并的基本逻辑和注意事项

- 合并本质：类似 SQL JOIN，基于公共键连接
- 核心函数：`pd.merge(left_df, right_df, on='key')`
- 注意键名一致、合并后数据量

## 五、合并参数 left, right, how

- `how`：`inner` / `left` / `right` / `outer`
- 类比 SQL：`how='left'` ≈ LEFT JOIN

## 六、合并参数 left_on, right_on, on

- `on`：两表键名相同时
- `left_on`、`right_on`：键名不同时
- 多键：`on=['key1', 'key2']`

## 七、groupby 分组

- 基本语法：`df.groupby('col').agg(func)`
- 分组后：聚合 `sum/mean/count`、遍历 `for name, group in df.groupby('col')`、筛选 `filter`

## 八、交叉表和透视表

- 交叉表：`pd.crosstab(df['a'], df['b'])` 统计频数
- 透视表：`pd.pivot_table(df, values='val', index='row', columns='col', aggfunc='mean')`
- 类比 Excel 数据透视表
