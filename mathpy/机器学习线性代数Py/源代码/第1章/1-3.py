import numpy as np
A = np.array([1, 2, 3, 4])
A_t = A[:, np.newaxis]
print(A_t)
print(A_t.shape)