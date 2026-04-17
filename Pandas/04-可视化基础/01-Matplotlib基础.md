# 可视化基础（Matplotlib）

> 覆盖：85-matplotlib绘图-图像组成 → 后续内容

## 一、matplotlib 绘图 - 图像组成

- Figure（画布）：整个绘图窗口
- Axes（坐标轴）：具体绘图区域
- Axis、Tick、Legend、Title
- 层级关系：Figure → Axes → Axis → Tick

## 二、画板、画布和就近原则

- 面向过程：`plt.plot()` / `plt.title()` 适合单图
- 面向对象：`fig, ax = plt.subplots()` → `ax.plot()` 适合多图
- 就近原则：在最近创建的 Figure/Axes 上操作
- 推荐：优先使用面向对象接口

## 三、网格设置

- 开启：`ax.grid(True)`
- 样式：`linestyle` / `color` / `alpha` / `axis='x'/'y'`

## 四、刻度界限

- `ax.set_xlim(left, right)` / `ax.set_ylim(bottom, top)`
- `ax.set_xticks([...])` / `ax.set_xticklabels([...])`

## 五、pandas 与 matplotlib 集成

- pandas 内置绘图：`df.plot()`
- 常用类型：`kind='line'` / `'bar'` / `'hist'` / `'scatter'`
- 散点图：`df.plot(kind='scatter', x='col1', y='col2')`
