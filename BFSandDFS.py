import collections
def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")
        for neighbour in graph.get(vertex, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  
    if start not in visited:  
        print(start, end=" ")
        visited.add(start)
        for next_node in graph[start]:  
            dfs(graph, next_node, visited)
    return visited
def get_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes in the graph: "))
    for _ in range(num_nodes):
        node = input("Enter node: ")
        neighbors = input(f"Enter neighbors of {node} (space-separated, or leave empty if none): ").split()
        graph[node] = neighbors 
    return graph
graph = get_graph()
start_node = input("Enter the start node for DFS: ")
print("\nDFS Traversal:")
dfs(graph, start_node)
start_node = int(input("Enter the starting node for BFS: "))
print("\nBFS Traversal:")
bfs(graph, start_node)

'''
 BFS (Breadth-First Search)
🧠 Theory
Explores the graph level by level (breadth-wise).

Uses a queue (FIFO) to keep track of nodes to visit.

Best for finding the shortest path in an unweighted graph.

Visits all neighbors before moving deeper.

BFS(graph, start):
    create an empty set visited
    create a queue Q
    enqueue start into Q
    mark start as visited

    while Q is not empty:
        current = dequeue Q
        process(current)
        for each neighbor of current:
            if neighbor not in visited:
                mark neighbor as visited
                enqueue neighbor into Q
Time: O(V + E)

Space: O(V) — for visited and queue

 DFS (Depth-First Search)
🧠 Theory
Explores the graph deeply first (depth-wise).

Uses a stack (LIFO) or recursion.

Goes as far as possible along one branch before backtracking.

Good for topological sorting, cycle detection, etc.
DFS(graph, start):
    create an empty set visited
    call DFS_Visit(start)

DFS_Visit(node):
    mark node as visited
    process(node)
    for each neighbor of node:
        if neighbor not in visited:
            DFS_Visit(neighbor)
Time: O(V + E)

Space: O(V) — for visited and stack/recursion

'''