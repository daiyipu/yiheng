import numpy as np

x = [2,2,4,8,4]
y = [2,6,6,8,8]
S = np.vstack((x,y))
print(np.cov(S))