# -*- coding:utf-8 -*-
import numpy as np
from scipy.stats import chi2_contingency
from scipy.stats import chi2
def jiashe(h, data):
    g, p, dof, expctd = chi2_contingency(data,True)
    if dof == 1:
        b = chi2.isf(h * 0.5, dof)
    elif dof == 0:
        print('自由度应该大于等�1')
    else:
        b = chi2.isf(h * 0.5, dof-1)
    if g > b:
        out = 1
    else:
        out = 0
    return g, p, dof, out, expctd

h1 = 0.05
data1 = np.array([[1265, 952], [380, 200]])
g, p, dof, out, expctd = jiashe(h1, data1)
print(g, p, dof, out)
print(expctd)
data2 = np.array([[1265, 952], [38, 20]])
g, p, dof, out, expctd = jiashe(h1, data2)
print(g, p, dof, out)
print(expctd)
