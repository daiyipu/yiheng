import numpy as np
A_1 = np.array([[1, 1, 0],
              [1, 0, 1]])

A_2 = np.array([[1, 2, -1],
              [2, 4, -2]])

A_3 = np.array([[1, 0],
              [0, 1],
              [0, -1]])

A_4 = np.array([[1, 2],
              [1, 2],
              [-1, -2]])

A_5 = np.array([[1, 1, 1],
              [1, 1, 2],
              [1, 2, 3]])

print(np.linalg.matrix_rank(A_1))
print(np.linalg.matrix_rank(A_2))
print(np.linalg.matrix_rank(A_3))
print(np.linalg.matrix_rank(A_4))
print(np.linalg.matrix_rank(A_5))