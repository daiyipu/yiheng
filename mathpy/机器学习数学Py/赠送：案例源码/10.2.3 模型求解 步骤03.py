from sympy import *
k = symbols("k")
f1 = 4745.45454545455 - 645.454545454546*0.67**(k + 1)
f2 = 645.454545454546*0.67**(k + 1) + 3954.54545454545
print(limit(f1, k, oo))
print(limit(f2, k, oo))