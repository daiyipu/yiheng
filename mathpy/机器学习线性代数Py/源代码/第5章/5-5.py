import numpy as np
from scipy import linalg

C = np.array([[6, 4],
              [4, 6]])

evalue, evector = linalg.eig(C)
print(evalue)
print(evector)