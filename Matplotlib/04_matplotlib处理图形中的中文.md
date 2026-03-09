# Matplotlib 处理图形中的中文

默认字体不支持中文，会显示为方框，需要设置中文字体。

## 方法一：全局设置

```python
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体  rcParams是 Python 可视化库 Matplotlib 中用于配置绘图全局参数的核心工具，相当于 Matplotlib 的“总设置面板”。
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

plt.plot([1, 2, 3], [1, 4, 9])
plt.title("中文标题")
plt.xlabel("横轴")
plt.ylabel("纵轴")
plt.show()
```
参数键	作用	量化常用值
图表尺寸（宽, 高）	（适合看K线趋势）
图片分辨率	（高清导出，用于报告）
线条粗细	（让趋势线更清晰）
是否显示网格	（看数值时更易定位）
网格透明度	（避免网格遮挡曲线）
## 常用中文字体

| 字体名 | 说明 |
|--------|------|
| SimHei | 黑体（Windows） |
| Microsoft YaHei | 微软雅黑 |
| SimSun | 宋体 |
| FangSong | 仿宋 |
| KaiTi | 楷体 |

## 方法二：局部设置

```python
from matplotlib import font_manager

font = font_manager.FontProperties(fname='C:/Windows/Fonts/simhei.ttf')
plt.title("中文标题", fontproperties=font)
```

## 要点

- 设置 `font.sans-serif` 后，所有文本默认使用该字体
- `axes.unicode_minus = False` 可正确显示负号「−」
