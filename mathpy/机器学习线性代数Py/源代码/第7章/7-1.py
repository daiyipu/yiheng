from sympy import integrate, cos, sin
from sympy.abc import x
import numpy as np

e = integrate(sin(x)*cos(x), (x, 0, 2*np.pi))
print(e.evalf())