import numpy as np
M= np.array([[12,9,-45],[7,4,15],[6,-3,21],[6,18,5]],dtype=float)
Q=np.zeros((4, 3))
j = 0
for a in M.T:
    b = np.copy(a)
    for i in range(0, j):
        b = b - np.dot(np.dot(Q[:, i].T, a), Q[:, i])
    e = b / np.linalg.norm(b)
    Q[:, j] = e
    j += 1
R = np.dot(Q.T, M)
np.set_printoptions(precision=3,suppress=True)
print('Gram-schmidt正交化变换结果')
print('Q矩阵：')
print(Q)
print('R矩阵：')
print(R)
print('矩阵的乘积：')
print(np.dot(Q,R))