# coding:utf-8
import numpy as np
e = np.mat([[0, 12, 50, float('inf'),39,41],
              [float('inf'), 0, 21, 18,float('inf'),11],
              [float('inf'), float('inf'), 0, 9,2,6],
              [float('inf'), float('inf'), float('inf'),0,13,2],
              [float('inf'), float('inf'), float('inf'),float('inf'),0,3],
              [float('inf'), float('inf'), float('inf'),float('inf'),float('inf'),0]])
L = e[:]
path = -np.ones((len(e), len(e)))

for i in range(len(e)):
    for j in range(len(e)):
        if e[i, j] == float('inf'):
            path[i][j] = -1
        elif e[i, j] == 0 :
            path[i][j] = 0
        else:
            path[i][j] = i
print('初始:')
print(L, '\n', path)
for a in range(len(e)):
    for b in range(len(e)):
        for c in range(len(e)):
            if (L[b, a] + L[a, c] < L[b, c]):
                L[b, c] = L[b, a] + L[a, c]
                path[b][c] = path[a][c]
print('结果:')
print(L, '\n', path)

# 原文链接：https: // blog.csdn.net / Lwenjiyou_ / article / details / 79548577