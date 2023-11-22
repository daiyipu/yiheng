import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)+2*np.sin(3*x)+2*np.cos(3*x)+4*np.sin(15*x)

x = np.linspace(0, 2*np.pi, 2048)
plt.scatter(x, f(x))
plt.grid()
plt.show()