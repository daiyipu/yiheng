import numpy as np
import scipy.stats
def KL_d(M, N):
    return scipy.stats.entropy(M, N)
M1 = np.array([0.8, 0.3, 0.12, 0.04],dtype=float)
N1 = np.array([0.7, 0.28, 0.08, 0.06],dtype=float)
print("M1,N1的KL散度：",KL_d(M1, N1))
M2 = np.array([0.9, 0.5, 0.15, 0.02],dtype=float)
N2 = np.array([0.8, 0.45, 0.07, 0.06],dtype=float)
print("M2,N2的KL散度：",KL_d(M2, N2))

