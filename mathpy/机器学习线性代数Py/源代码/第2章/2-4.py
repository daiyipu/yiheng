import numpy as np
from scipy import linalg

A = np.array([[1, 2, 3],
              [1, -1, 4],
              [2, 3, -1]])

y = np.array([14, 11, 5])
x = linalg.solve(A, y)
print(x)