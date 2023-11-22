# encoding:utf-8
import networkx as nx
# 使用dijkstra_path算法找到所有对最短路径长度。
G = nx.DiGraph() # 建立一个空的有向图G
G.add_weighted_edges_from(
    [('0', '1', 12), ('0', '2', 50), ('0', '4', 39), ('0', '5', 41),
     ('1', '2', 21), ('1', '3', 18), ('1', '5', 11),
     ('2', '3', 9), ('2', '4', 2), ('2', '5', 6),
     ('3', '4', 13), ('3', '5', 2), ('4', '5', 3)])
# 边和节点信息
edge_labels = nx.get_edge_attributes(G, 'weight')
labels = {'0': 'A', '1': 'B', '2': 'C', '3': 'D','4': 'E','5': 'F'}
pred, dist = nx.dijkstra_predecessor_and_distance(G, '0')
print('\n加权图最短路径前驱和长度:\n ', pred,'\n', dist)
# 返回G中从源到目标的最短加权路径,要求边权重必须为数值
print('\nG中从源0到目标4的最短加权路径: ', nx.dijkstra_path(G, '0', '4'))
print('\nG中从源0到目标4的最短加权路径的长度: ',
      nx.dijkstra_path_length(G, '0','4'))  # 最短路径长度