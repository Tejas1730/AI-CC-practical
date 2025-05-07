class Graph:
    def __init__(self, vertices):
        self.V = vertices 
        self.edges = [] 	

    def add_edge(self, u, v, w):
        self.edges.append((w, u, v)) 

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        self.edges.sort() 
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        mst = []
        i = 0  
        e = 0 
        while e < self.V - 1:
            w, u, v = self.edges[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:  # If no cycle
                mst.append((u, v, w))
                self.union(parent, rank, x, y)
                e += 1
        print("\nMinimum Spanning Tree (MST) Edges:")
        total_cost = 0
  

        for u, v, weight in mst:
            print(f"{u} -- {v} == {weight}")
            total_cost += weight
            print(f"Total Minimum Cost: {total_cost}")
V = int(input("Enter the number of vertices: "))
E = int(input("Enter the number of edges: "))

g = Graph(V)
print("Enter edges in format: source destination weight")
for _ in range(E):
    u, v, w = map(int, input().split())
    g.add_edge(u, v, w)
g.kruskal_mst()


'''
Kruskal’s Algorithm – Theory
🎯 Goal:
To find a subset of edges that:

Forms a tree that includes every vertex.

Has minimum possible total edge weight.

Contains no cycles.

This subset is called the Minimum Spanning Tree (MST).

🔍 Key Concepts:
Greedy Approach: Always pick the smallest weight edge that doesn’t form a cycle.

Disjoint Set Union (DSU) or Union-Find is used to detect cycles.

1. Sort all the edges in increasing order of their weight.
2. Initialize a disjoint-set (Union-Find) for all vertices.
3. MST = empty set
4. For each edge (u, v) in sorted edge list:
    a. If u and v are in different sets:
        - Add edge (u, v) to MST
        - Union the sets of u and v
    b. If u and v are already connected (same set), skip to avoid a cycle.
5. Stop when MST has (V - 1) edges.

Sorting edges: O(E log E)

DSU operations: O(E × α(V)) ≈ O(E) (α is inverse Ackermann function)

Overall: O(E log E)
'''