class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)
        self._heapify_up()

    def pop(self):
        if len(self.heap) == 0:
            return None
        self._swap(0, len(self.heap) - 1)
        item = self.heap.pop()
        self._heapify_down()
        return item

    def _heapify_up(self):
        idx = len(self.heap) - 1
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[parent][0] <= self.heap[idx][0]:
                break
            self._swap(parent, idx)
            idx = parent

    def _heapify_down(self):
        idx = 0
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


def get_graph_input():
    print("Enter the graph (format: city1 city2 cost), type 'done' when finished:")
    graph = {}
    while True:
        line = input()
        if line.lower() == "done":
            break
        try:
            city1, city2, cost = line.split()
            cost = int(cost)
            graph.setdefault(city1, {})[city2] = cost
            graph.setdefault(city2, {})[city1] = cost  # If undirected
        except:
            print("Invalid format. Please enter: city1 city2 cost")
    return graph


def get_heuristic_input():
    print("Enter heuristics (format: city cost), type 'done' when finished:")
    heuristics = {}
    while True:
        line = input()
        if line.lower() == "done":
            break
        try:
            city, cost = line.split()
            heuristics[city] = int(cost)
        except:
            print("Invalid format. Please enter: city cost")
    return heuristics


def a_star_search(start, goal, graph, heuristics):
    pq = MinHeap()
    pq.push((heuristics[start], 0, start, [start]))  # (f(n), g(n), city, path)
    visited = set()

    while not pq.is_empty():
        _, cost, city, path = pq.pop()
        if city in visited:
            continue
        visited.add(city)

        if city == goal:
            print("\nOptimal A* Path:", " -> ".join(path))
            print("Total Cost:", cost)
            return

        for neighbor, travel_cost in graph.get(city, {}).items():
            if neighbor not in visited:
                new_cost = cost + travel_cost
                f_n = new_cost + heuristics.get(neighbor, float('inf'))
                pq.push((f_n, new_cost, neighbor, path + [neighbor]))

    print("\nNo valid path found from", start, "to", goal)


# Main Program
dict_gn = get_graph_input()
dict_hn = get_heuristic_input()

start_city = input("Enter the start city: ")
goal_city = input("Enter the goal city: ")

if start_city not in dict_gn or goal_city not in dict_hn:
    print("Invalid city name. Please enter valid cities.")
else:
    a_star_search(start_city, goal_city, dict_gn, dict_hn)
