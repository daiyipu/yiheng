import numpy as np
from scipy import linalg
A = np.array([[1, 35, 0],
              [0, 2, 3],
              [0, 0, 4]])

A_n = linalg.inv(A)
print(A_n)
print(np.dot(A, A_n))