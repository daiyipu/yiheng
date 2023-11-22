from sympy import *
g,r,t = symbols("g,r,t")
Q=-(30-g*t)*(2+r*t)+2*t+60
dify = diff(Q, t)
print(dify)
