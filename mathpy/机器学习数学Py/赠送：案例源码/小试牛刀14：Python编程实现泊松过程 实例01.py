import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
rate = 6
n = np.arange(0,13)
y = stats.poisson.pmf(n,rate)
print (y)
print ("the probability of number 8:" ,y[8])
plt.plot(n, y, 'o--')
plt.title('Poisson', fontsize=18)
plt.xlabel('Number of Big Truck')
plt.ylabel('Probability of  number ', fontsize=18)
plt.show()