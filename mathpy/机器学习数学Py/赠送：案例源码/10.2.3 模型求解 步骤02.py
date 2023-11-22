import numpy as np
from sympy import *
P1 =  np.array([[ 0.76822128, -0.70710678],[ 0.6401844, 0.70710678]])
k = symbols("k")
P2 = np.linalg.inv(P1)
s1 = [[1,0],[0,0.67**(k+1)]]
a = [4100,4600]
s = np.dot(np.dot( np.dot(P1,s1),P2) ,a)
print(s)