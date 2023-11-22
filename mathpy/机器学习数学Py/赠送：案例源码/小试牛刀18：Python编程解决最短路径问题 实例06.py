# encoding:utf-8
import networkx as nx
G = nx.DiGraph() # 建立一个空的有向图G
G.add_weighted_edges_from(
    [('0', '1', 12), ('0', '2', 50), ('0', '4', 39), ('0', '5', 41),
     ('1', '2', 21), ('1', '3', 18), ('1', '5', 11),
     ('2', '3', 9), ('2', '4', 2),('2', '5', 6),
    ('3', '4', 13), ('3', '5', 2), ('4', '5', 3)])
# 边和节点信息
edge_labels = nx.get_edge_attributes(G, 'weight')
labels = {'0': 'A', '1': 'B', '2': 'C', '3': 'D','4': 'E','5': 'F'}
print("'0'到 '4'的最短加权路径:",nx.astar_path(G, '0', '4'))
print("'0'到 '4'的最短加权路径的长度:",nx.astar_path_length(G, '0', '4'))

# https://networkx.github.io/documentation/networkx-1.10/reference/algorithms.html
# https://blog.csdn.net/qq_40875849/article/details/100524437