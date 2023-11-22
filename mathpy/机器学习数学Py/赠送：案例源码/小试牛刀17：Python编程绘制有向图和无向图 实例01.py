# encoding:utf-8
import networkx as nx
import matplotlib.pyplot as plt
# 建立无向图
G = nx.Graph()
G.add_node('A')  # 添加一个节点A
G.add_nodes_from(['B', 'C', 'D', 'E'])  # 加点集合
H = nx.path_graph(6)  # 返回由6个节点挨个连接的无向图，所以有5条边
G.add_nodes_from(H)  # 创建一个子图H加入G
G.add_node(H)  # 直接将图作为节点
#访问节点
print('图中所有的节点：\n', G.nodes())
print('图中节点的个数：', G.number_of_nodes())
#删除节点
G.remove_node(1)    #删除指定节点
G.remove_nodes_from(['B', 'C', 'D'])    #删除集合中的节点
print('\n图中所有的节点：\n', G.nodes())
print('图中节点的个数：', G.number_of_nodes())
nx.draw(G, with_labels=True)
G.clear() #清空图
#创建无向图
#添加边
F = nx.Graph()
F.add_edge(7,8)   #一次添加一条边
#等价于
e=(9,10)        #e是一个元组
F.add_edge(*e) #这是python中解包裹的过程
F.add_edges_from([(1,9),(2,7),(8,6),(11,10)])     #通过添加list来添加多条边
#通过添加任何ebunch来添加边
F.add_edges_from(H.edges()) #不能写作F.add_edges_from(H)
nx.draw(F, with_labels=True)
plt.savefig("17-a.png")
plt.show()
print('\n图中所有的边：\n', F.edges())
print('图中边的个数：', F.number_of_edges())
#删除边
F.remove_edge(1,2)
F.remove_edges_from([(1,9), (8,6)])
print('\n图中所有的边：\n', F.edges())
print('图中边的个数：', F.number_of_edges())
nx.draw(F, with_labels=True)
plt.savefig("17-b.png")
plt.show()
F.clear() #清空图