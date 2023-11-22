import numpy as np

eng, mat, phy = np.loadtxt('score.csv', delimiter=',',
                           usecols=(0, 1, 2), unpack=True)
S = np.vstack((eng,mat,phy))
print(np.cov(S))