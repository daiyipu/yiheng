import numpy as np

A=[[0, 0, 0, 2, 2],
   [0, 0, 0, 3, 3],
   [0, 0, 0, 1, 1],
   [1, 1, 1, 0, 0],
   [2, 2, 2, 0, 0],
   [5, 5, 5, 0, 0],
   [1, 1, 1, 0, 0]]

U, sigma, VT = np.linalg.svd(A)
U_T_2x7 = U.T[:2,:]
print(np.dot(U_T_2x7,A))
VT_2x5=VT[:2,:]
print(np.dot(VT_2x5,np.mat(A).T).T)