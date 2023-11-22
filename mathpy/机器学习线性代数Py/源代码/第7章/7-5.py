import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 128)
y = np.sin(x)+2*np.sin(3*x)+2*np.cos(3*x)+4*np.sin(15*x)

xf = np.arange(len(y))               #离散频率
xf_half = xf[range(int(len(x)/2))]   #由于对称性，只取一半区域
yf = abs(fft(y))/len(x)              #执行完fft后，对各频率的能量归一化处理
yf_half = yf[range(int(len(x)/2))]   #由于对称性，只取一半区间

plt.plot(xf_half, yf_half)
plt.show()