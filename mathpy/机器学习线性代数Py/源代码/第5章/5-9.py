import numpy as np

A=[[0, 0, 0, 2, 2],
   [0, 0, 0, 3, 3],
   [0, 0, 0, 1, 1],
   [1, 1, 1, 0, 0],
   [2, 2, 2, 0, 0],
   [5, 5, 5, 0, 0],
   [1, 1, 1, 0, 0]]

U, sigma, VT = np.linalg.svd(A)
A_1 = sigma[0]*np.dot(np.mat(U[:, 0]).T, np.mat(VT[0, :]))
A_2 = sigma[1]*np.dot(np.mat(U[:, 1]).T, np.mat(VT[1, :]))
print(A_1+A_2)