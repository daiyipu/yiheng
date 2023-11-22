import scipy
from scipy.stats import pearsonr
x = scipy.array([3, 6, 8, 9, 12])
y = scipy.array([4, 7, 6, 11, 15])
r_row, p_value = pearsonr(x, y)
print(r_row )
print(p_value)
import numpy as np
x = np.array([3, 6, 8, 9, 12])
y = np.array([4, 7, 6, 11, 15])
n=len(x)
s_xy = np.sum(np.sum(x*y))
s_x = np.sum(np.sum(x))
s_y = np.sum(np.sum(y))
s_x1 = np.sum(np.sum(x*x))
s_y1 = np.sum(np.sum(y*y))
pe = (n*s_xy-s_x*s_y)/np.sqrt((n*s_x1-s_x*s_x)*(n*s_y1-s_y*s_y))
print(pe)