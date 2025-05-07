INF = 9999999
N = int(input("Enter the number of vertices in the graph: "))
print("\nEnter the adjacency matrix row by row (use 0 for no edge):")
G = []
for i in range(N):
    row = list(map(int, input().split()))
    G.append(row)
selected_node = [False] * N
no_edge = 0
selected_node[0] = True
print("\nEdge : Weight")
while no_edge < N - 1:
    minimum = INF
    a = b = 0
    for m in range(N):
        if selected_node[m]:  # If node is already selected
            for n in range(N):
                if (not selected_node[n]) and G[m][n]:  # If not selected and edge exists
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a, b = m, n
    print(f"{a} - {b} : {G[a][b]}")
    selected_node[b] = True
    no_edge += 1


'''
Prim’s Algorithm – Theory
🎯 Goal:
Build a Minimum Spanning Tree (MST) by growing the tree one vertex at a time:

Always pick the smallest edge that connects a vertex in the MST to a vertex outside it

 Key Idea:
Start with any node.

Repeatedly add the smallest edge that connects the MST to a new vertex.

Continue until all vertices are included in the MST.

📋 Input:
A connected, undirected graph with V vertices and E weighted edges

1. Initialize a set MST[] to store MST vertices.
2. Create a min-priority queue (min-heap) to pick the edge with the smallest weight.
3. Start from any vertex (e.g., vertex 0):
   - Set its key = 0 and all others to ∞.
4. While MST doesn't include all vertices:
   a. Pick the vertex `u` with the smallest key value not yet in MST.
   b. Include `u` in MST.
   c. For every adjacent vertex `v` of `u`:
       - If `v` not in MST and weight(u, v) < key[v], update key[v]
5. Output the selected edges and their total weight.

🧮 Time and Space Complexity
Using Min-Heap:
Time Complexity: O((V + E) log V)
(with priority queue and adjacency list)

Space Complexity: O(V) for MST set and O(E) for edge list
'''