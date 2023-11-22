# encoding:utf-8
import matplotlib.pyplot as plt
import networkx as nx
tu = [[0, 12, 50, float('inf'),39,41],
      [12, 0, 21, 18,float('inf'),11],
      [50, 21, 0, 9,2,6],
      [float('inf'), 18, 9,0,13,2],
      [39, float('inf'), 2,13,0,3],
      [41, 11, 6,2,3,0]]
print('邻接矩阵为')
for i in tu :
    print(i)
print('节点数:%d个' % (len(tu)))
result = []
# 选择节点
s_node = [0]
# 备选节点
c_node = [i for i in range(1, len(tu))]
while len(c_node) > 0:
    start, end, small = 0, 0, float('inf')
    for i in s_node:
        for j in c_node:
            if tu[i][j] < small:
                small = tu[i][j]
                start = i
                end = j
    result.append([start, end, small])
    s_node.append(end)
    c_node.remove(end)
print('最小生成树prim算法的结果：\n',result)
tree=[]
for i in result:
    i =tuple(i)
    tree.append(i)
mtg = nx.Graph()
mtg.add_weighted_edges_from(tree)
print('图中所有的节点:', mtg.nodes())
print('图中节点的个数:', mtg.number_of_nodes())
pos = nx.spring_layout(mtg)
nx.draw(mtg,pos,
        arrows=True,
        with_labels=True,
        nodelist=mtg.nodes(),
        style='dashed',
        edge_color='b',
        width=2,
        node_color='r',
        alpha=0.5)
plt.savefig("19-a.png")
plt.show()