import sys
import matplotlib.pyplot as plt
import networkx as nx

from DijkstrasAlgorithm import *
from DataSource import *

# Execute Dijkstra Algorithm 
tableNodes, finalPath = DijkstrasAlgorithm(graph1).run().values()

print("============== The Shortest Path discovered ===================")
print(finalPath)

# Make the List which specifies the edges from the Final Shortest Path
finalPathEdges = []
for k, nodo in enumerate(finalPath):
    if k+1 >= len(finalPath):
        break
    finalPathEdges.append((finalPath[k], finalPath[k+1]))

# Create a Visual Graph
G = nx.Graph()

# Add Nodes to the Visual Graph
add_nodes_from = [(node[0], {"label":node[0]}) for node in graph1["tableNodes"]]
G.add_nodes_from(add_nodes_from)

# Add Edges to the Visual Graph
add_edges_from = [(edge[0], edge[1], {"weight": edge[2]}) for edge in graph1["tableEdges"]]
G.add_edges_from(add_edges_from)

# Make Node Labels
node_labels = {n: (d["label"]) for n,d in G.nodes(data=True)}

# Set position of Node Labels
pos_node_labels = {}
for node,(x,y) in graph1["posNodes"].items():
    pos_node_labels[node] = (x+0.5, y-1.5)

# Make Edge Labels
edge_labels = {(u,v): d["weight"] for u,v,d in G.edges(data=True)}

# Customize color of Nodes included within the Final Shortest Path
node_colors = ["green" if n in finalPath else "lightgray" for n in G.nodes()]

# make good order of edges !!THIS IS UNIQUE BECAUSE OF THE LIBRARY Networkx!!
good_ordered_edges_for_graph = []
for (a,b) in G.edges():
    for (x,y,z) in graph1["tableEdges"]:
        if (a == x and b == y) or (b == x and a == y):
            good_ordered_edges_for_graph.append((x,y))
            break

# Customize color of Edges included within the Final Shortest Path
edge_colors = ["green" if n in finalPathEdges else "lightgray" for n in good_ordered_edges_for_graph]

# Draw all Nodes and its customized colors
nx.draw(G, pos=graph1["posNodes"], with_labels=True, 
    node_color=node_colors, node_size=3000, 
    font_color="white", font_size=20, 
    font_family="Times New Roman", edge_color=edge_colors,
    width=5)

# Draw all Node Labels
nx.draw_networkx_labels(G, pos=pos_node_labels, labels=node_labels, 
    font_color="black", font_size=12, 
    font_family="Times New Roman")

# Draw all Edge Labels
nx.draw_networkx_edge_labels(G, pos=graph1["posNodes"], edge_labels=edge_labels, 
    label_pos=0.5)

plt.margins(0.2)
plt.show()