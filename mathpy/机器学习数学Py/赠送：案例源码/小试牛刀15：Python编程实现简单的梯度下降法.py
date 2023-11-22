def fun(x1, x2): #定义函数t
    t = x1**2 + x2**4 + (2*x2+x1)**2
    return t
def di(x1, x2):  #x1, x2关于函数t 的一阶导数
    t1 = 2*x1+4*(2*x1+x2)
    t2 = 4*x1**3+2*(2*x1+x2)
    return t1, t2
# 梯度下降算法
def grad(n):         #计算通过梯度下降的流程迭代n次后的极小值点
    alpha = 0.001    # 学习率
    x1, x2 = 1, 1    # 初始值
    y1 = fun(x1, x2)
    for i in range(n):
        di1, di2 = di(x1, x2)
        x1 = x1 - alpha * di1   #梯度下降中最重要的步骤，通过一阶导数迭代x1
        x2 = x2 - alpha * di2   #梯度下降中最重要的步骤，通过一阶导数迭代x2
        y2 = fun(x1, x2)
        if y1 - y2 < 1e-7:
            return x1, x2, y2
        if y2 < y1:
            y1 = y2

    return x1, x2, y2
x1, x2, y = grad(100000)
print('极小值y:',y,'x1,x2坐标点：',x1,x2,)


