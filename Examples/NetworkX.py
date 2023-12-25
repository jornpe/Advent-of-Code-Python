import networkx as nx
import matplotlib.pyplot as plt



# building the graph
G = nx.Graph()
G.add_edge("A", "B", weight=4)
G.add_edge("B", "D", weight=2)
G.add_edge("A", "C", weight=3)
G.add_edge("C", "D", weight=4)

# using matplot to do the acuall drawing.
nx.draw(G)
plt.show()

# Not sure if weight is needed here. It gives same path regardless.
print(nx.shortest_path(G, "A", "D", weight="weight"))
