import numpy as np
import cvxpy as cvx
# 1.变量定义Variable和Parameter
a = cvx.Parameter(4,nonneg=True)
a.value = np.array([3,4,6,7],dtype=np.float)
b = cvx.Variable(6)#列向量,6维
# 矩阵变量
c = cvx.Variable((6, 1))
d = cvx.Variable(2, complex=False)
e = cvx.Variable((6,6),PSD=True)
f = cvx.Variable(2, complex=True)
g = cvx.Variable(2, imag=True)

# 2.运算规则
c = np.arange(6)
x = cvx.Variable(6)
print("(c*x).shape:",(c*x).shape) 
print("vx.multiply(c,x).shape:",cvx.multiply(c,x).shape) #元素乘
c = np.arange(6).reshape((6,1))
x = cvx.Variable((6,1))
print("(c.T*x).shape:",(c.T*x).shape)
print("cvx.multiply(c,x).shape:",cvx.multiply(c,x).shape)
c = np.arange(12).reshape((6,2))
x = cvx.Variable((6,2))
print("(c.T*x).shape:",(c.T*x).shape)
print("cvx.multiply(c,x).shape:",cvx.multiply(c,x).shape)
c = np.arange(6)
x = cvx.Variable((6,6))
print("(c*x).shape:",(c*x).shape)
print("(c.T*x).shape:",(c.T*x).shape)
print("(c*x*c).shape:",(c*x*c).shape)
print("(c.T*x*c).shape:",(c.T*x*c).shape)

# 3.定义约束
x = cvx.Variable(6)
constraints = []
constraints.append(x >= 0)
constraints.append(x <= 10)
# 只有一部分向量sum(x[:3]) <= 3
constraints.append(cvx.sum(x[:3]) <= 3)
for constr in constraints: #
    print("变量是 DCP:", constr, constr.is_dcp())
n=6
x = cvx.Variable((n,n))
A = np.random.rand(n,n)
constraints = []
#添加正半定约束
constraints +=[(x >> 0)]
constraints += [(cvx.trace(cvx.multiply(A,x))>=0)]
n=6
x = cvx.Variable((n,n))
A = np.random.rand(n,n)
constraints = []
#添加正半定约束
constraints +=[(x >> 0),(cvx.trace(cvx.multiply(A,x))>=0)]
x = cvx.Variable(2, name='x')
y = cvx.Variable(3, name='y')
z = cvx.Variable(2, name='z')
t = cvx.Variable()
exp = x + z
scalar_exp = 3.0+t
#二阶锥约束 SOC ->cvx.norm(exp)<=scalar_exp
constr = cvx.SOC(scalar_exp, exp)
constraints = []
constraints.append(constr)
#PSD变量
H = cvx.Variable((3, 3), PSD=True)
F1 = np.array([[0, 0, 1/2], [0, 0, 0], [1/2, 0, 1]])
F2 = np.array([[0, 0, 0], [0, 0, 1/2], [0, 1/2, 1]])
constraints = []
constraints.append(H + F1>>0)
constraints.append(H + F2>>0)
objective = cvx.Minimize(cvx.trace(H))

# 4.不同的求解器求解
# 创建3个标量优化变量。
t = cvx.Variable(3)
t1 = t[0]
t2 = t[1]
t3 = t[2]
objective1 =-4*t1-6*t3
# 创建约束条件
constraints = [18*t1-t2+6*t3<=1,
               2*t1+4*t3<=1,
               10*t1+t2<=1,
               t<=1]
# 创建目标函数
obj1 = cvx.Minimize(objective1)
#建立问题和解决问题
prob1 = cvx.Problem(obj1, constraints)
print("\nsolvers:",cvx.installed_solvers(),'\n')
solvers=[cvx.SCS,cvx.CVXOPT,cvx.GLPK,cvx.GLPK_MI,cvx.OSQP]
for solver in solvers:
    prob1.solve(solver=solver)  # Returns the optimal value.
    print("solver:", solver)
    print("status:", prob1.status)
    print("optimal value", prob1.value)
    print("optimal var", t.value,'\n')



