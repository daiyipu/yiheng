from numpy import *
import numpy as np
A=[[0.85,0.18],[0.15,0.82]]
D,P = linalg.eig(A)
print(D,P)