# -*- coding:utf-8 -*-
import numpy as np
import math
import matplotlib.pyplot as plt
u = 0  # 均值μ
sig = math.sqrt(0.15)  # 标准差δ
sig1 = math.sqrt(0.3)  # 标准差δ
x = np.linspace(u - 3 * sig, u + 3 * sig, 40)
x_1 = np.linspace(u - 6 * sig, u + 6 * sig, 40)
y_sig = np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2 * math.pi) * sig)
y_sig1 = np.exp(-(x_1 - u) ** 2 / (2 * sig1 ** 2)) / (math.sqrt(2 * math.pi) * sig1)
plt.plot(x, y_sig, "b-", linewidth=3)
plt.plot(x_1, y_sig1, "r-", linewidth=3)
plt.grid(True)
plt.show()
