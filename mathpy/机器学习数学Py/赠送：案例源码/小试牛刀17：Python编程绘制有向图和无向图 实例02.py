# encoding:utf-8
import networkx as nx
import matplotlib.pyplot as plt
# 建立有向图
G = nx.DiGraph() # 建立一个空的有向图G
G.add_node('A')  # 添加一个节点A
G.add_nodes_from(['B', 'C', 'D', 'E'])  # 加点集合
H = nx.path_graph(8)  # 返回由8个节点挨个连接的有向图，所以有7条边
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
G.clear() #清空图

#创建有向图
#添加边
F = nx.DiGraph()# 创建有向图
F.add_edge(9,10)   #一次添加一条边
#等价于
e=(11,12)        #e是一个元组
F.add_edge(*e) #这是python中解包裹的过程
#通过添加任何ebunch来添加边
F.add_edges_from(H.edges()) #不能写作F.add_edges_from(H)
F.add_edges_from([(2,9),(7,11)])  #通过添加list来添加多条边
nx.draw(F, with_labels=True)
plt.savefig("17-c.png")
plt.show()
print('\n图中所有的边：\n', F.edges())
print('图中边的个数：', F.number_of_edges())
#删除边
F.remove_edge(2,3)
F.remove_edges_from([(5,6), (9,10)])
print('\n图中所有的边：\n', F.edges())
print('图中边的个数：', F.number_of_edges())
nx.draw(F, with_labels=True)
plt.savefig("17-d.png")
plt.show()
F.clear() #清空图
