import os
import networkx as nx
from input_data import load_data
from matplotlib import pyplot as plt

# Train on CPU (hide GPU) due to memory constraints
os.environ['CUDA_VISIBLE_DEVICES'] = ""

adj, features, graph_temp = load_data('cora')
graph = nx.from_dict_of_lists(graph_temp)


print("First time to draw the cora dataset:")
nx.draw_networkx(graph)
plt.show()


print("\n\nSecond time to draw the cora dataset:")
nx.draw_networkx(graph)
plt.show()

print("\n\nThird time to draw the cora dataset:")
nx.draw_networkx(graph)
plt.show()

print("FUCK!\nFUCK!\nFUCK!\nFUCK!\nFUCK!\nThe results are different every time.")