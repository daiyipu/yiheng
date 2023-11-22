#coding:gbk
from numpy import *
import numpy as np
import copy
# EM算法：步骤1
def my_e(Sigma,k,N,P,Mu,X):
    for i in range(0,N):
        Denom = 0
        for j in range(0,k):
            Denom += np.exp(-1.0 / (2.0 * Sigma ** 2) * (X[i] - Mu[j]) ** 2)
            # Denom += math.exp((-1/(2*(float(Sigma**2))))*(float(X[0,i]-Mu[j]))**2)
        for j in range(0,k):
            Numer = np.exp(-1.0 / (2.0 * Sigma ** 2) * (X[i] - Mu[j]) ** 2)
            # Numer = math.exp((-1/(2*(float(Sigma**2))))*(float(X[0,i]-Mu[j]))**2)
            P[i,j] = Numer / Denom
# EM算法：步骤2
def my_m(k,N,P,X):
    for j in range(0,k):
        Numer = 0
        Denom = 0
        for i in range(0,N):
            Numer += P[i, j] * X[i]
            Denom += P[i, j]
            # Numer += P[i,j]*X[0,i]
            # Denom += P[i,j]
        Mu[j] = Numer / Denom
Sigma = 5
Mu1 = 55
Mu2 = 22
k = 2
N = 1200
iter_num = 500
Epsilon = 0.0001
# X = np.zeros((1, N))
X = mat(zeros((N,1)))
Mu = np.random.random(2)
P = np.zeros((N, k))
for i in range(0, N):
    if np.random.random(1) > 0.5:
        X[i] = np.random.normal() * Sigma + Mu1
    else:
        X[i] = np.random.normal() * Sigma + Mu2
print (u"初始<u1,u2>:", Mu)
for i in range(iter_num):
    Old_Mu = copy.deepcopy(Mu)
    my_e(Sigma,k,N,P,Mu,X)
    my_m(k,N,P,X)
    print (i,Mu)
    if sum(abs(Mu-Old_Mu)) < Epsilon:
        break
