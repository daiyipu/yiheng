import numpy as np
import hmmlearn.hmm as hmm
states= ["晴","阴","雨"]
ob = {"浇水":0,"除草":1,"劈柴":2,"休息":3}
model = hmm.MultinomialHMM(n_components=len(states))
s =[]
for line in open ("h1.txt",encoding='utf-8'):
    r =[i.split('_')for i in line[:-2].split('\t')]
   # print(r)
    L =[]
    for i in r:
        L.append(i[0])
    L1 = [ob[j] for j in L]
    s.append(L1)
model.fit(s)
print(model.startprob_)
print(model.transmat_)
print(model.emissionprob_)
# 运用viterbi预测的问题
se = np.array([[0, 1, 1, 0, 2, 3, 3]]).T
ob1 = ["浇水","除草","劈柴","休息"]
logprod, box_index = model.decode(se, algorithm='viterbi')
print("当天的事件:", end="")
print(" ".join(map(lambda t: ob1[t], [0, 1, 1, 0, 2, 3, 3])))
print("天气:", end="")
print(" ".join(map(lambda t: states[t], box_index)))
print("概率值:", end="")
print(np.exp(logprod)) 