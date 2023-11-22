import numpy as np
A = np.array([[1, 2],
               [3, 4],
               [5, 6]])
x = np.array([[4, 5]]).T
print(np.dot(A, x))