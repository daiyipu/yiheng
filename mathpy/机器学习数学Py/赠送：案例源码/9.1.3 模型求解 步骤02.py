# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
def fun(g,r,t):
    Q=-(30-g*t)*(2+r*t)+2*t+60
    return Q
def di(g,r,t):
    Q1 = g*(r*t + 2) + r*(g*t - 30) + 2
    return Q1
def grad(g,r,n):
    alpha = 0.1    # 学习�
    t = 2    # 初始�
    y1 = fun(g,r,t)
    for i in range(n):
        di1= di(g,r,t)
        t = t - alpha * di1
        y2 = fun(g,r,t)
        if y1 - y2 < 1e-7:
            return t,y2
        if y2 < y1:
            y1 = y2
    return t, y2
g = 0.04
r = 0.1
t, y = grad(g,r,100000)
print('取整后： 极小值y:',round(y),'t坐标点：',round(t))
x = np.linspace(0.05, 250, 500)
y=-(30-g*x)*(2+r*x)+2*x+60
plt.plot(x, y, ls="-", lw=2, label="plot figure")
plt.legend()
plt.show()
