from sympy import integrate, cos, sin
from sympy.abc import x
import numpy as np

e1 = integrate(sin(2*x)*cos(5*x), (x, 0, 2*np.pi))
e2 = integrate(sin(4*x)*cos(0*x), (x, 0, 2*np.pi))
e3 = integrate(sin(x)*cos(2*x), (x, 0, 2*np.pi))
print(e1.evalf())
print(e2.evalf())
print(e3.evalf())