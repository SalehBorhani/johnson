import matplotlib.pyplot as plt
import networkx as nx
import my_networkx as my_nx
import main

graph = [[0, -5, 2, 3],
        [0, 0, 4, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0]]

f_graph = main.JohnsonAlgorithm(graph)
G = nx.DiGraph()

edge_list = []
for i in range(len(graph)):
    for j in range(len(graph)):
        edge_list.append((i, j, {'w': f'{f_graph[i][j]}'}))     
       

#edge_list = [(1,2,{'w':'5'}),(2,1,{'w':'-3'}),(2,3,{'w':'0'}),(3,1,{'w':'2'}),
#             (3,4,{'w':'3'}),(4,3,{'w':'-1'}),(1,5,{'w':'-7'}),(5,1,{'w':'-2'}),
#             (3,5,{'w':'1'}),(5,4,{'w':'2'})]

G.add_edges_from(edge_list)
pos=nx.spring_layout(G,seed=5)
fig, ax = plt.subplots()
nx.draw_networkx_nodes(G, pos, ax=ax)
nx.draw_networkx_labels(G, pos, ax=ax)

curved_edges = [edge for edge in G.edges() if reversed(edge) in G.edges()]
straight_edges = list(set(G.edges()) - set(curved_edges))
nx.draw_networkx_edges(G, pos, ax=ax, edgelist=straight_edges)
arc_rad = 0.25
nx.draw_networkx_edges(G, pos, ax=ax, edgelist=curved_edges, connectionstyle=f'arc3, rad = {arc_rad}')


edge_weights = nx.get_edge_attributes(G,'w')
curved_edge_labels = {edge: edge_weights[edge] for edge in curved_edges}
straight_edge_labels = {edge: edge_weights[edge] for edge in straight_edges}
my_nx.my_draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=curved_edge_labels,rotate=False,rad = arc_rad)
nx.draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=straight_edge_labels,rotate=False)

plt.show()
