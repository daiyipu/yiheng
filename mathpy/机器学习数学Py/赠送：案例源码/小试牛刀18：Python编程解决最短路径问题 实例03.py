# encoding:utf-8
import networkx as nx
import matplotlib.pyplot as plt
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
# 生成节点位置
pos = nx.spring_layout(G)
# 把节点画出来
nx.draw_networkx_nodes(G, pos, node_color='g', node_size=500, alpha=0.8)
# 把边画出来
nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.8, edge_color='b')
# 把节点的标签画出来
nx.draw_networkx_labels(G, pos, labels, font_size=20)
# 把边权重画出来
nx.draw_networkx_edge_labels(G, pos, edge_labels,font_size=10)
# 显示graph
plt.savefig("18-a.png")
plt.show()


# 注:输出中的矩阵不是按照节点'0', '1', '2','3','4', '5'排序,而是'0', '1', '2', '4', '5', '3'