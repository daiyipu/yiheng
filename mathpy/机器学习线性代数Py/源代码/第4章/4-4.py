import numpy as np
from scipy import linalg

A = np.array([[6, -2, 1],
              [0, 4, 0],
              [0,0,6]])

evalue, evector = linalg.eig(A)
print(evalue)
print(evector)