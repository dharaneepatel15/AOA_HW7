import heapq

def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    parents = {node: None for node in graph}
    
    priority_queue = [(0, source)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances, parents


def get_shortest_path(target, parents):
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = parents[current]
    return path[::-1]

def build_adjacency_list(vertices, edges):
    graph = {vertex: [] for vertex in vertices}
    for source, destination, weight in edges:
        graph[source].append((destination, weight))
    return graph

# 1. Raw Data
my_vertices = ['A', 'B', 'C', 'D']
my_edges = [
    ('A', 'B', 4),
    ('A', 'C', 1),
    ('C', 'B', 2),
    ('B', 'D', 5),
    ('C', 'D', 8)
]

# 2. Build Graph Adjacency List
my_graph_input = build_adjacency_list(my_vertices, my_edges)

# 3. Run Algorithm
start_node = 'A'
distances, parents = dijkstra(my_graph_input, start_node)

# 4. Extract Path (Arguments correctly match: target_node first, then parents)
target_node = 'D'
shortest_path = get_shortest_path(target_node, parents)

# 5. Print Results
print(f"Shortest path from {start_node} to {target_node}: {shortest_path}")
print(f"Total travel cost/weight: {distances[target_node]}")
