import heapq
graph = {
    'A': [('B', 36), ('C', 61)],
    'B': [('A', 36), ('D', 31)],
    'C': [('A', 61), ('D', 32), ('L', 80)],
    'D': [('B', 31), ('C', 32), ('E', 52), ('F', 31)],
    'E': [('D', 52), ('G', 43)],
    'F': [('D', 31), ('G', 31), ('K', 112), ('L', 31)],
    'G': [('E', 43), ('F', 31), ('H', 20)],
    'H': [('G', 20), ('I', 40), ('J', 12)],
    'I': [('H', 40), ('J', 45)],
    'J': [('H', 12), ('I', 45), ('K', 36)],
    'K': [('F', 112), ('J', 36), ('M', 32)],
    'L': [('C', 80), ('F', 31), ('M', 102)],
    'M': []
}
heuristic = {
    'A': 223, 'B': 222, 'C': 166, 'D': 192, 'E': 165,
    'F': 136, 'G': 122, 'H': 111, 'I': 100, 'J': 60,
    'K': 32, 'L': 102, 'M': 0
}
def a_star(graph, heuristic, start, goal):
    open_list = [(0 + heuristic[start], 0, start, [])]
    heapq.heapify(open_list)

    visited = set()

    while open_list:
        _, cost, current, path = heapq.heappop(open_list)

        path = path + [current]

        if current == goal:
            return path, cost

        if current in visited:
            continue

        visited.add(current)

        for neighbor, distance in graph[current]:
            if neighbor not in visited:
                new_cost = cost + distance
                heapq.heappush(open_list, (new_cost + heuristic[neighbor], new_cost, neighbor, path))

    return None, float('inf')

path, cost = a_star(graph, heuristic, 'A', 'M')

print("Path:", " -> ".join(path))
print("Total Cost:", cost)
