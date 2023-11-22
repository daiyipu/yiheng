# encoding:utf-8
import networkx as nx
import matplotlib.pyplot as plt
# # 使用Floyd算法找到所有对最短路径长度。
G = nx.Graph() # 建立一个空的无向图G
G.add_weighted_edges_from(
    [('0', '1', 12), ('0', '2', 50), ('0', '4', 39), ('0', '5', 41),
     ('1', '2', 21), ('1', '3', 18), ('1', '5', 11),
     ('2', '3', 9), ('2', '4', 2),('2', '5', 6),
    ('3', '4', 13), ('3', '5', 2), ('4', '5', 3)])
# 边和节点信息
edge_labels = nx.get_edge_attributes(G, 'weight')
labels = {'0': '0', '1': '1', '2': '2', '3': '3','4': '4','5': '5'}
# 生成节点位置
pos = nx.spring_layout(G)
# 把节点画出来
nx.draw_networkx_nodes(G, pos, node_color='r', node_size=500, alpha=0.8)
# 把边画出来
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5,
                       edge_color=['b', 'r', 'b', 'r', 'r', 'b', 'r'])
# 把节点的标签画出来
nx.draw_networkx_labels(G, pos, labels, font_size=16)
# 把边权重画出来
nx.draw_networkx_edge_labels(G, pos, edge_labels)
plt.savefig("19-c.png")
# 显示graph
plt.show()
# 最小生成树

# 求得最小生成树,algorithm使用prim
KA = nx.minimum_spanning_tree(G, algorithm='prim')
print('prim算法的结果:\n',KA.edges(data=True))
# 直接拿到构成最小生成树的边,algorithm使用prim
mst = nx.minimum_spanning_edges(G, algorithm='prim', data=False)
edgelist = list(mst)
print('prim算法的结果中最小生成树的边:\n',edgelist,'\n')

# 求得最小生成树,algorithm使用kruskal，如果不写出algorithm参数，其默认值也是kruskal
KA = nx.minimum_spanning_tree(G, algorithm='kruskal')
print('kruskal算法的结果:\n',KA.edges(data=True))
# 直接拿到构成最小生成树的边,algorithm使用kruskal
# 如果不写出algorithm参数，其默认值也是kruskal
mst = nx.minimum_spanning_edges(G, algorithm='kruskal', data=False)
edgelist = list(mst)
print('kruskal算法的结果中最小生成树的边:\n',edgelist)