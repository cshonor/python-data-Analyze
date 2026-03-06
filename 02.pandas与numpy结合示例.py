"""
Pandas + NumPy 结合示例

展示如何将 NumPy 数组与 Pandas 配合使用：创建数据、运算、绘图。
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. NumPy 生成数据，Pandas 组织成表格
x = np.linspace(0, 2 * np.pi, 100)
df = pd.DataFrame({
    "x": x,
    "sin": np.sin(x),
    "cos": np.cos(x),
})

print("DataFrame 前 5 行:\n", df.head())

# 2. 用 NumPy 运算，结果写回 Pandas
df["sin2"] = np.sin(x) ** 2

# 3. Pandas 的 describe 结合 NumPy 数据
print("\n统计:\n", df.describe())

# 4. 用 Matplotlib 画 Pandas 列
plt.plot(df["x"], df["sin"], label="sin")
plt.plot(df["x"], df["cos"], label="cos")
plt.legend()
plt.title("Pandas + NumPy 绘图")
plt.show()
