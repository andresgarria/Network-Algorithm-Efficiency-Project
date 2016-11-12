import networkx as nx
import matplotlib.pyplot as plt

# Create graph
G=nx.Graph()

# Add nodes
G.add_node(1)
G.add_nodes_from([2,3])

H=nx.path_graph(10)
# G.add_nodes_from(H)
G.add_node(H)

G.add_edge(1,2)
e=(2,3)
G.add_edge(*e)

nx.draw(G)
plt.show()

# G.add_edges_from([(1,2),(1,3)])

# After removing all nodes and edges
# G.clear()
# >>> G.nodes()
# >>> G.edges()
# >>> G.neighbors(1)
