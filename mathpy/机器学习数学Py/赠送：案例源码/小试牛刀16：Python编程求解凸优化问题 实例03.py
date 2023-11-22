import cvxpy as cvx
import numpy
# Problem data.
m = 20
n = 4
numpy.random.seed(10)
A = numpy.random.randn(m, n)
b = numpy.random.randn(m)

# 构造问题
x = cvx.Variable(n)
objective = cvx.Minimize(cvx.sum_squares(A*x - b))
prob = cvx.Problem(objective,
                   [0 <= x, x <= 10])
print("Optimal value", prob.solve())
print("Optimal var")
print(x.value)

