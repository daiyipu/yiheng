import numpy as np
from scipy import linalg

A = np.array([[2, 1],
              [1, 2]])
evalue, evector = linalg.eig(A)
print(evalue)
print(evector)