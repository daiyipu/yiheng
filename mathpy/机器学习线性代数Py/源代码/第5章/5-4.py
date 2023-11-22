import numpy as np

x = [2,2,4,8,4]
y = [2,6,6,8,8]

x = x - np.mean(x)
y = y - np.mean(y)
S = np.vstack((x,y))
print(S)
print(np.cov(S))