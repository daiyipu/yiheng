import numpy as np
def cross(M, N):
    return -np.sum(M * np.log(N) + (1 - M) * np.log(1 - N))
M1 = np.asarray([0.8, 0.3, 0.12, 0.04],dtype=float)
N1 = np.array([0.7, 0.28, 0.08, 0.06],dtype=float)
print("M1,N2交叉熵：",cross(M1,N1))




