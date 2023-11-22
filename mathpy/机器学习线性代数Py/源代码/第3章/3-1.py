import numpy as np
from scipy import linalg

A = np.array([[2, 1],
              [1, 2],
              [1, 4]])

b = np.array([[4],
              [3],
              [9]])

A_T_A = np.dot(A.T,A)
x = np.dot(np.dot(linalg.inv(A_T_A),A.T),b)
print(x)