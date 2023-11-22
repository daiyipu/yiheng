from sympy import *
def fun(c1,c2,c3,r,t,Q):
    C= c1/t+(c2*(Q**2))/(2*r*t)+(c3*((r*t-Q)**2))/(2*r*t)
    return C
def di(c1,c2,c3,r,t,Q):
    C1 = -Q**2*c2/(2*r*t**2) - c1/t**2 + c3*(-Q + r*t)/t - c3*(-Q + r*t)**2/(2*r*t**2)
    C2 = Q*c2/(r*t) + c3*(2*Q - 2*r*t)/(2*r*t)
    return C1,C2
def grad(c1,c2,c3,r,n):
    alpha = 0.1    # 学习率
    alpha1 = 0.4  # 学习率
    t,Q = 1,1    # 初始值
    y1 = fun(c1,c2,c3,r,t,Q)
    for i in range(n):
        di1, di2 = di(c1,c2,c3,r,t, Q)
        t = t - alpha * di1
        Q = Q - alpha1 * di2
        y2 = fun(c1,c2,c3,r,t,Q)
        # print(t)
        # print(y2)
        if y1 - y2 < 1e-10:
            return t,Q,y2
        if y2 < y1:
            y1 = y2
    return t,Q,y2
c1,c2,c3,r=4000,1.2,0.15,120
t,Q,y = grad(c1,c2,c3,r,100000)
print('计算得到 极小值y:',y,'\n','t，Q坐标点：',t,Q)
# 验证
t1=sqrt((2*c1/r*c2)*((c2+c3)/c3))
q1=sqrt((2*c1*r/c2)*(c3/(c2+c3)))
print('*'*50)
print('微分法验证 t，Q坐标点：',t1,q1)
