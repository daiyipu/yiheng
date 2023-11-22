# encoding:utf-8
import cvxpy as cvx
import numpy as np
# 创建 two scalar optimization variables.
x = cvx.Variable(4)
c = cvx.Parameter(shape=(4,))
c.value = np.array([-4,0,-17,-2])

A = cvx.Parameter(shape=(4,4))
A.value = np.array([[14,-6,8,7],
                    [1,0,4,11],
                    [12,3,0,23],
                    [5,2,11,0]])
b = cvx.Parameter(shape=(4,))
b.value = np.array([1,1,1,1])
objective =c.T*x

# 创建两个约束条件
constraints = [A*x<=b,
               x<=6]
# 创建目标函数
obj = cvx.Minimize(objective)

#建立问题和解决问题
prob = cvx.Problem(obj, constraints)
print ("prob is DCP:", prob.is_dcp())
prob.solve(solver=cvx.CVXOPT)  # Returns the optimal value.
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x.value)