import heapq
def dijkstra(graph, start):
    # Priority queue for selecting the minimum weight edge (Greedy)
    pq = [(0, start)]  # (cost, node)
    shortest_paths = {node: float('inf') for node in graph}  # Set all distances to infinity
    shortest_paths[start] = 0  # Distance to source is 0
    while pq:
        current_cost, current_node = heapq.heappop(pq)
        for neighbor, weight in graph[current_node].items():
            new_cost = current_cost + weight
            if new_cost < shortest_paths[neighbor]:  # Greedy Choice: Pick minimum cost
                shortest_paths[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))
    return shortest_paths

graph = {}
num_nodes = int(input("Enter number of nodes: "))
num_edges = int(input("Enter number of edges: "))
print("Enter edges in format: source destination weight")
for _ in range(num_edges):
    u, v, w = input().split()
    w = int(w)
    if u not in graph:
        graph[u] = {}
   
    if v not in graph:
        graph[v] = {}
    graph[u][v] = w  # Directed graph
    graph[v][u] = w  # Undirected graph (remove for directed)
start_node = input("Enter the start node: ")
shortest_distances = dijkstra(graph, start_node)
print("\nShortest distances from node", start_node)
for node, distance in shortest_distances.items():
    print(f"{start_node} -> {node} = {distance}")

'''
Purpose:
To find the shortest path from a single source vertex to all other vertices in a weighted graph with non-negative edge weights.

Works on graphs with non-negative weights.

Finds shortest path from a source node to all other nodes.

Uses a greedy approach: always picks the nearest unvisited node.

Often implemented using a priority queue (min-heap) for efficiency.

1. Initialize:
    - Set dist[] = ∞ for all vertices
    - Set dist[src] = 0
    - Create a priority queue (min-heap) and insert (0, src)

2. While the priority queue is not empty:
    a. Pop (distance, current_node) from the queue
    b. For each neighbor of current_node:
        i. If dist[neighbor] > dist[current_node] + weight(current_node → neighbor):
            - Update dist[neighbor] = dist[current_node] + weight
            - Push (dist[neighbor], neighbor) into the queue

3. Return dist[] array
'''