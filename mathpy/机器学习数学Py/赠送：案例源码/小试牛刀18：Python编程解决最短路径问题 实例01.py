import numpy as np
def start_to_end(P,startpoint,endpoint,p,m):
    if startpoint <m:
        if startpoint==endpoint:
            p.append(startpoint)
        else:
            p.append(endpoint)
            start_to_end(P,startpoint,P[endpoint],p,m)
    return p
G = np.array([[0, 12, 50, float('inf'),39,41],
              [float('inf'), 0, 21, 18,float('inf'),11],
              [float('inf'), float('inf'), 0, 9,2,6],
              [float('inf'), float('inf'), float('inf'),0,13,2],
              [float('inf'), float('inf'), float('inf'),float('inf'),0,3],
              [float('inf'), float('inf'), float('inf'),float('inf'),float('inf'),0]])

label = ['A','B','C','D','E','F']

n = G.shape[0]
P1 = []
A = []
for index, item in enumerate(label):
    for index1, item1 in enumerate(label):
        Dist = [[] for i in range(n)]
        Path = [[] for i in range(n)]
        flag = [[] for i in range(n)]
        i = 0
        while i < G.shape[0]:
            Dist[i] = G[label.index(item)][i]
            flag[i] = 0
            if G[label.index(item)][i] < float('inf'):
                Path[i] = label.index(item)
            else:
                Path[i] = -1
            i += 1
            
        flag[label.index(item)] = 1
        Path[label.index(item)] = 0
        Dist[label.index(item)] = 0
        i= 1
        while i < G.shape[0]:
            MinDist = float('inf')
            j = 0
            while j < G.shape[0]:
                if flag[j] == 0 and Dist[j] < MinDist:
                    t = j
                    MinDist = Dist[j]
                j += 1
            flag[t] = 1
            End = 0
            MinDist = float('inf')

            while End < G.shape[0]:
                if flag[End] == 0:
                    if G[t][End] < MinDist and Dist[t] + G[t][End] < Dist[End]:
                        Dist[End] = Dist[t] + G[t][End]
                        Path[End] = t
                End += 1
            i += 1
        v_to_end = []  # 存储从源点到终点的最短路径
        if (index1==len(label)-1):
            P1.append(Path)
        path = start_to_end(Path, label.index(item), label.index(item1), v_to_end, len(label)-1)
        dist = Dist[ label.index(item1)]
        if dist ==float('inf') or dist ==0:
            pass
        else:
            Path=[]
            for k in range(len(path)):
                Path.append(label[path[len(path)-1-k]])
            print('从顶点{}到顶点{}的最短路径为：{}最短路径长度为：{}'.format(item,item1,Path,dist))
    A.append(Dist)
P1 = np.array(P1)
A = np.array(A)
print(A, '\n', P1)

