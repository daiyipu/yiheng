import numpy as np
from scipy import linalg
B = np.array([[1, 0, 2],
              [0, 1, 3],
              [1, 1, 5]])
B_n = linalg.inv(B)
print(B_n)