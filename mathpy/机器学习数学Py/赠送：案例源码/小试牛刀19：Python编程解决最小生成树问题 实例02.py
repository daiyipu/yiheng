# encoding:utf-8
# https://blog.csdn.net/olizxq/article/details/82831863?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522159487987819724839243290%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=159487987819724839243290&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-1-82831863.pc_ecpm_v3_pc_rank_v3&utm_term=%E6%9C%80%E5%B0%8F%E7%94%9F%E6%88%90%E6%A0%91+python
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
b_list = []
for i in range(len(tu)):
    for j in range(i, len(tu)):
        if tu[i][j] < float('inf'):
            b_list.append([i, j, tu[i][j]])  # 按[begin, end, weight]形式加入
b_list.sort(key=lambda a: a[2])  # 已经排好序的边集合
g = [[i] for i in range(len(tu))]
for b in b_list:
    for i in range(len(g)):
        if b[0] in g[i]:
            m = i
        if b[1] in g[i]:
            n = i
    if m != n:
        result.append(b)
        g[m] = g[m] + g[n]
        g[n] = []
print('最小生成树kruskal算法的结果：\n',result)

tree=[]
for i in result:
    i =tuple(i)
    tree.append(i)
mtg = nx.Graph()
mtg.add_weighted_edges_from(tree)
print('图中所有的节点:', mtg.nodes())
print('图中节点的个数:', mtg.number_of_nodes())
pos = nx.spring_layout(mtg)
nx.draw(mtg, pos,
        arrows=True,
        with_labels=True,
        nodelist=mtg.nodes(),
        style='dashed',
        edge_color='b',
        width=2,
        node_color='r',
        alpha=0.5)
plt.savefig("19-b.png")
plt.show()