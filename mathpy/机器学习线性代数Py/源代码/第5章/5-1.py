import numpy as np

eng, mat, phy = np.loadtxt('score.csv', delimiter=',',
                           usecols=(0, 1, 2), unpack=True)
print(eng.mean(), mat.mean(), phy.mean())
print(np.cov(eng), np.cov(mat), np.cov(phy))