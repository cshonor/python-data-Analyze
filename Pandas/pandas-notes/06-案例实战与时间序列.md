# 案例实战与时间序列

> 覆盖：71-美国人口密度分析 → 84-重采样和时间差

## 一、案例实战：美国人口密度分析

- 州简称与全称处理：映射字典 + `map()` 批量替换
- state 缺失值补全：推断、外部匹配或标记为未知
- 密度计算：`人口密度 = 人口数 / 面积`，注意单位转换

## 二、案例实战：美国选举政治献金分析

- 本地文件读取汇总：循环读取 CSV，`pd.concat` 拼接
- 党派支持度分析：`groupby('party')['donation'].sum()`，占比计算
- 时间序列分析：`pd.to_datetime`，按周期 `dt.to_period('M')` 分组
- 捐赠者分析：`value_counts`、大额筛选、关联分析

## 三、时间序列基础

### 1. 时间戳和时间段

- 时间戳 `Timestamp`：具体时间点
- 时间段 `Period`：时间区间
- `pd.Timestamp('2024-01-01')` / `pd.Period('2024-01', freq='M')`

### 2. 批量生成时间索引

- `pd.date_range(start, end, freq='D'/'H'/'W'/'M')`

### 3. 时间字符串批量转换

- `pd.to_datetime(df['date_str'], format='%Y-%m-%d')`，`errors='coerce'`

### 4. 脏时间数据处理

- 缺失插值、格式统一、时区对齐

### 5. DatetimeIndex 的访问机制

- `df.index.year` / `month` / `day`，切片 `df.loc['2024-01':'2024-03']`

### 6. 时间戳和时间索引的属性

- `ts.year` / `ts.month` 等，`index.freq` / `index.tz`

### 7. 重采样和时间差

- 重采样：`df.resample('M').mean()` 降采样，`ffill()` 升采样
- 时间差：`index.diff()`，`end_date - start_date` 返回 `Timedelta`
