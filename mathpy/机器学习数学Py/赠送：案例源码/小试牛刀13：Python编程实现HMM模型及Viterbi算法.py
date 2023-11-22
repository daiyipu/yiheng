import numpy as np
def viterbi( pi,obs, A, B, Q):
    s = len(Q)
    n = len(A)
    d = np.zeros((s, n))
    pre = np.zeros((n, s))
    for i in range(n):
        d[0][i] = pi[i] * B[i][(Q[0])]
        pre[i][0] = i
    for j in range(1, s):
        new = np.zeros((n, s))
        for k in range(n):
            p = -0.1
            for m in range(n):
                tmp = d[j-1][m] * A[m][k] * B[k][Q[j]]
                if tmp > p:
                    p = tmp
                    state = m
                    d[j][k] = p
                    for m in range(j):
                        new[k][m] = pre[state][m]
                    new[k][j] = k
        pre = new
    de = -1
    pre_s = 0
    for i in range(n):
        if d[s-1][i] > de:
            de = d[s-1][i]
            pre_s = i
    return pre[pre_s]
# 测试
np.random.seed(14)
pi = np.array([0.4, 0.25, 0.35])
A = np.array([
    [0.7, 0.1, 0.2],
    [0.3, 0.15, 0.55],
    [0.2, 0.5, 0.3]
])
B = np.array([
    [0.3, 0.7],
    [0.7, 0.3],
    [0.45, 0.55]
])
obs = ['白','绿']
Q = [0,0,0, 1,0,1,1]
# 开始计算
state_seq = viterbi( pi,obs, A, B, Q)
print("观测状态为：白白白绿白绿绿")
print("最终结果为:", end='')
print(state_seq)
state = ['养鸡场1', '养鸡场2', '养鸡场3']
for i in range(len(state_seq)):
    print(state[int(state_seq[i])],end='\t')