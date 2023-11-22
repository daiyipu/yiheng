import numpy as np
from scipy import linalg

A = np.array([[1, 0, 0],
              [0, 2, 0],
              [0, 0, 5]])
evalue, evector = linalg.eig(A)
print(evalue)
print(evector)