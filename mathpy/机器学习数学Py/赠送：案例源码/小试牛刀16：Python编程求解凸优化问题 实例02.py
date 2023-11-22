# encoding:utf-8
import cvxpy as cvx
x = cvx.Variable()
y = cvx.Variable()
# DCP problems.
prob1 = cvx.Problem(cvx.Minimize(cvx.square(x - y)),
                    [x + 2*y >= 0])
prob2 = cvx.Problem(cvx.Maximize(cvx.sqrt(x - y)),
                [5*x - 3 == y,
                 cvx.square(x) <= 2])
print("prob1 is DCP:", prob1.is_dcp())
print("prob2 is DCP:", prob2.is_dcp())
# 非DCP问题
# 一个非DCP 目标函数
obj = cvx.Maximize(cvx.square(x))
prob3 = cvx.Problem(obj)
print("prob3 is DCP:", prob3.is_dcp())
print("prob3的目标函数是 DCP:", obj.is_dcp())

# 一个非DCP 约束条件
constraints= [cvx.sqrt(x) <= 2]
prob4 = cvx.Problem(cvx.Minimize(cvx.square(x)),
                    constraints)
print ("prob4 is DCP:", prob4.is_dcp())
print ("prob4的目标函数:", cvx.square(x).curvature)
print ("prob4的约束条件是 DCP:", constraints[0].is_dcp())

try:
    prob1.solve(solver=cvx.CVXOPT)  # Returns the optimal value.
    print("\n prob1 status:", prob1.status)
    print("optimal value", prob1.value)
except Exception as e:
    print('\n 不能求解prob1')
    print(e)

try:
    prob2.solve(solver=cvx.CVXOPT)  # Returns the optimal value.
    print("\n prob2 status:", prob2.status)
    print("optimal value", prob2.value)
except Exception as e:
    print('\n 不能求解prob2')
    print(e)

try:
    prob3.solve(solver=cvx.CVXOPT)  # Returns the optimal value.
    print("\n prob3 status:", prob3.status)
    print("optimal value", prob3.value)
except Exception as e:
    print('\n 不能求解prob3')
    print(e)


try:
    prob4.solve(solver=cvx.CVXOPT)  # Returns the optimal value.
    print("\n prob4 status:", prob4.status)
    print("optimal value", prob4.value)
except Exception as e:
    print('\n 不能求解prob4')
    print(e)
