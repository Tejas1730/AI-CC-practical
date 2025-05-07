class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        item = self.heap.pop()
        self._heapify_down(0)
        return item

    def _heapify_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[parent][0] <= self.heap[idx][0]:
                break
            self._swap(parent, idx)
            idx = parent

    def _heapify_down(self, idx):
        while 2 * idx + 1 < len(self.heap):
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = left
            if right < len(self.heap) and self.heap[right][0] < self.heap[left][0]:
                smallest = right
            if self.heap[idx][0] <= self.heap[smallest][0]:
                break
            self._swap(idx, smallest)
            idx = smallest

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def is_empty(self):
        return not self.heap


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = MinHeap()
    open_list.push((heuristic(start, goal), 0, start, []))
    visited = set()

    while not open_list.is_empty():
        f, g, current, path = open_list.pop()
        if current in visited:
            continue
        visited.add(current)
        path = path + [current]

        if current == goal:
            return path

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                neighbor = (nx, ny)
                if neighbor not in visited:
                    open_list.push((g + 1 + heuristic(neighbor, goal), g + 1, neighbor, path))

    return None


def get_user_input():
    print("Enter grid row by row (use 0 for open, 1 for obstacle), type 'done' when finished:")
    grid = []
    while True:
        line = input()
        if line.lower() == 'done':
            break
        row = list(map(int, line.strip().split()))
        grid.append(row)

    start = tuple(map(int, input("Enter start position (e.g., 0 0): ").split()))
    goal = tuple(map(int, input("Enter goal position (e.g., 4 3): ").split()))

    return grid, start, goal


# Main Program
grid, start, goal = get_user_input()
path = astar(grid, start, goal)

if path:
    print("Path found:")
    for p in path:
        print(p)
else:
    print("No path found.")
'''
Purpose:
To find the shortest (or optimal) path from a start node to a goal node in a weighted graph using heuristics to guide the search efficiently.
A* combines the strengths of:

Dijkstra’s Algorithm (which always finds the shortest path),

and Greedy Best-First Search (which uses heuristics for faster traversal).

A* uses:

g(n): the cost from the start node to the current node n.

h(n): a heuristic estimate of the cost from n to the goal.

f(n) = g(n) + h(n): the estimated total cost of the path through n.
A heuristic is a function that estimates the remaining cost to the goal.

It must be:

Admissible: never overestimates the true cost.

Consistent (Monotonic): ensures f(n) values are non-decreasing.

Examples:

Manhattan distance for grids.

Euclidean distance for geometric problems.
1. Initialize:
    - Open set (priority queue): contains the start node.
    - g(start) = 0
    - f(start) = h(start)
    - Came_from = {} (used to reconstruct path)

2. While the open set is not empty:
    a. current = node in open set with lowest f(current)
    b. If current == goal:
          Return path by backtracking through came_from

    c. Remove current from open set
    d. For each neighbor of current:
        - tentative_g = g(current) + cost(current, neighbor)
        - If tentative_g < g(neighbor):
            - came_from[neighbor] = current
            - g(neighbor) = tentative_g
            - f(neighbor) = g(neighbor) + h(neighbor)
            - If neighbor not in open set:
                Add neighbor to open set

3. If goal not reached:
    Return failure (no path)

'''