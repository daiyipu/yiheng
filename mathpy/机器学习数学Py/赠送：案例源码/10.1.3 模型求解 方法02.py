import numpy as np
A1 = [[1,-0.4,-0.3],
     [-0.7,0.88,-0.2],
     [-0.6,-0.15,1]]
b = np.transpose([70000,95000,50000])# 转置
# 求解未知参数矩阵X
X = np.linalg.solve(A1,b)
print("方程组的解：\n",X)