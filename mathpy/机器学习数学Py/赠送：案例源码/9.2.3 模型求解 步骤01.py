from sympy import *
t ,c1,c2,c3,r,Q = symbols("t,c1,c2,c3,r,Q ")
C = c1/t + (c2*(Q**2))/(2*r*t)+(c3*((r*t-Q)**2))/(2*r*t)
dify1= diff(C, t)
dify2 = diff(C, Q)
print(dify1)
print(dify2)