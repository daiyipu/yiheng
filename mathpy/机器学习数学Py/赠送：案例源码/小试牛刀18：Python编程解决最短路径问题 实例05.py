# encoding:utf-8
import networkx as nx
# 使用Floyd算法找到所有对最短路径长度。
G = nx.DiGraph() # 建立一个空的有向图G
G.add_weighted_edges_from(
    [('0', '1', 12), ('0', '2', 50), ('0', '4', 39), ('0', '5', 41),
     ('1', '2', 21), ('1', '3', 18), ('1', '5', 11),
     ('2', '3', 9), ('2', '4', 2),('2', '5', 6),
    ('3', '4', 13), ('3', '5', 2), ('4', '5', 3)])
# 边和节点信息
edge_labels = nx.get_edge_attributes(G, 'weight')
labels = {'0': 'A', '1': 'B', '2': 'C', '3': 'D','4': 'E','5': 'F'}
# 计算最短路径长度
lenght = nx.floyd_warshall(G, weight='weight')
# 计算最短路径上的前驱与路径长度
predecessor, distance1 = nx.floyd_warshall_predecessor_and_distance(G, weight='weight')
# 计算两两节点之间的最短距离,并以numpy矩阵形式返回
distance2 = nx.floyd_warshall_numpy(G, weight='weight')
print("节点:",list(distance1))
print("最短加权路径矩阵:\n",distance2)
print( "'0'到 '4'的最短加权路径:\n",nx.reconstruct_path('0', '4', predecessor))

# 注:输出中的矩阵不是按照节点'0', '1', '2','3','4', '5'排序,而是'0', '1', '2', '4', '5', '3'