import numpy as np

x = [2,2,4,8,4]
y = [2,6,6,8,8]

x = x - np.mean(x)
y = y - np.mean(y)
A = np.vstack((x,y))
p_1 = [0.707, 0.707]
p_2 = [-0.707, 0.707]
P = np.vstack((p_1,p_2))
print(A)
print(np.dot(P,A))