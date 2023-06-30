# Implementation of Johnson's algorithm in Python3

# Import function to initialize the dictionary
from collections import defaultdict
import heapq
INT_MAX = float('Inf')

# Function that returns the vertex 
# with minimum distance 
# from the source
def Min_Distance(dist, visit):

    (minimum, Minimum_Vertex) = (INT_MAX, 0)
    for vertex in range(len(dist)):
        if minimum > dist[vertex] and visit[vertex] == False:
            (minimum, minVertex) = (dist[vertex], vertex)

    return Minimum_Vertex


# Dijkstra Algorithm for Modified
# Graph (After removing the negative weights)
def dijkstra(graph, chosen_vertex): 
    #print(graph) 
    heap = [(0, chosen_vertex)] 
    visited = set() 
    dist = {} 
 
    while heap: 
        (w, u) = heapq.heappop(heap) 
        if u in visited: 
            continue 
        visited.add(u) 
        dist[u] = w 
        #print(f"new dist {dist}") 
        for v, weight in graph[u].items(): 
            if v not in visited: 
                next_w = weight + w 
                heapq.heappush(heap, (next_w, v)) 
 
    return dist

# Function to calculate shortest distances from source
# to all other vertices using Bellman-Ford algorithm
def bellman_ford(graph, extra_vertex): 
    # using float(inf) to use 'inf' as a number 
    # create a dict with inf element at first for all vertex 
    dist = {v: float('inf') for v in graph} 
    dist[extra_vertex] = 0 
    #print(f"dist: {dist}") 
 
    # relax: 
    for _ in range(len(graph) - 1): 
        for u in graph: 
            for v, w in graph[u].items(): 
                if dist[u] != float('inf') and dist[u] + w < dist[v]: 
                    dist[v] = dist[u] + w 
        # print(dist) 
 
    for u in graph: 
        for v, w in graph[u].items(): 
            if dist[u] != float('inf') and dist[u] + w < dist[v]: 
                raise Exception( 
                    "The circumference of the graph cannot be negative") 
 
   # 'dist' is a dictionary that show the value of vertex after relaxing 
    return dist 
## Function to implement Johnson Algorithm
#def JohnsonAlgorithm(graph):
#
#    edges = []
#
#    # Create a list of edges for Bellman-Ford Algorithm
#    for i in range(len(graph)):
#        for j in range(len(graph[i])):
#
#            if graph[i][j] != 0:
#                edges.append([i, j, graph[i][j]])
#
#    # Weights used to modify the original weights
#    Alter_weigts = bellman_ford(edges, graph)
#
#    Altered_Graph = [[0 for p in range(len(graph))] for q in
#                    range(len(graph))]
#
#    # Modify the weights to get rid of negative weights
#    for i in range(len(graph)):
#        for j in range(len(graph[i])):
#
#            if graph[i][j] != 0:
#                Altered_Graph[i][j] = (graph[i][j] +
#                        Alter_weigts[i] - Alter_weigts[j]);
#
#    # Run Dijkstra for every vertex as source one by one
#    final_graph = []
#    for source in range(len(graph)):
#        final_graph.append(dijkstra(graph, source))
#
#    return final_graph    
#
#
def johnson(graph): 
    # Add a new vertex with weight 0 to every other vertex 
    s = 's' 
    graph_len = len(graph) 
 
    # add the element to dictionary 
    graph[s] = {v: 0 for v in graph} 
 
    # showing the ui for the Proximity matrix after adding 's' vertex 
    #create_Proximity_matrix( 
    #graph, graph_len, title="after adding extra vertex") 
 
    # Run Bellman Ford algorithm from the new vertex s 
    h = bellman_ford(graph, s) 
    if h is None: 
        return None 
 
    # Recompute edge weights using the potentials from Bellman-Ford 
    for u in graph: 
        for v in graph[u]: 
            graph[u][v] += h[u] - h[v] 
 
    # Run Dijkstra's algorithm from every vertex 
    shortest_paths = {} 
    for u in graph: 
        shortest_paths[u] = dijkstra(graph, u) 
 
        # Add back the potentials to get the actual distances 
        for v in shortest_paths[u]: 
            shortest_paths[u][v] += h[v] - h[u] 
 
    # delete extra vertex from graph 
    del shortest_paths[s] 
 
    #create_Proximity_matrix(shortest_paths, graph_len, 
                            #title="final matrix with johnsone algorithm")
    
    return shortest_paths
