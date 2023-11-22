import numpy as np
np.set_printoptions(precision=4, suppress=True)
M= np.array([[12,9,-45],[7,4,15],[6,-3,21],[6,18,5]],dtype=float)
s = 4
t = 3
Q = np.identity(s)
R = np.copy(M)
for j in range(s - 1):
    x = R[j:, j]
    E = np.zeros((4, 3))
    E = np.zeros_like(x)
    b = x - E
    d = b / np.linalg.norm(b)
    Q_j = np.identity(s)
    Q_j[j:, j:] -= 2.0 * np.outer(d, d)
    R = np.dot(Q_j, R)
    Q = np.dot(Q, Q_j)
np.set_printoptions(precision=3,suppress=True)
print('Householder变换结果')
print('Q矩阵：')
print(Q)
print('R矩阵：')
print(R)
print('矩阵的乘积：')
print(np.dot(Q,R))