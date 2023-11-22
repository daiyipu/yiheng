import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
data = stats.poisson.rvs(mu=6, loc=0, size=1100)
target = [i for i in data if i==8]
#打印该时刻通过8辆大货车的实验次数
print("the probability of number 8:" , str(len(target)/1100.0))
plt.hist(data,bins = 12, range=(0,13),density = True)
plt.title('Poisson', fontsize=18)
plt.xlabel('Number of Big Truck')
plt.ylabel('Probability of number ', fontsize=18)
plt.show()