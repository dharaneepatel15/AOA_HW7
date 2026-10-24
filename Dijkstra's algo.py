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
        
        # UNCOMMENT THIS LINE FOR TWO-WAY ROADS:
        graph[destination].append((source, weight))
        
    return graph


# 1. Raw Data
my_vertices = list(range(1,23))
my_edges = [(17,11,1), (11,1,1), (1,2,1), (2,3,1), (3,4,1), (4,5,1), (5,6,2),     # Texas Ave
         (9,10,1), (10,11,1), (11,12,2), (12,13,2), (13,14,2), (14,15,1),      # University / Raymond Stotzer
         (19,9,2), (9,8,1), (8,7,1), (7,6,2),                                  # Hwy 6
         (8,3,2), (2,21,1), (21,20,2), (13,21,1), (21,22,2),                   # Harvey Rd, George Bush, Wellborn
         (16,14,1), (14,20,1), (20,22,1), (22,5,1),                            # Harvey Mitchell Pkwy
         (5,7,1), (16,17,2), (17,18,2), (18,10,2), (18,19,2)]                  # other roads
start_node, target_nodes = 1, [6, 8, 9, 15, 16, 22]

# 2. Build Graph Adjacency List
my_graph_input = build_adjacency_list(my_vertices, my_edges)

# 3. Run Algorithm
# start_node = 'A'
distances, parents = dijkstra(my_graph_input, start_node)


for target in target_nodes:
    shortest_path = get_shortest_path(target, parents)
    print(f"Shortest path from {start_node} to {target}: {shortest_path}")
    print(f"Total travel cost/weight: {distances[target]}")
    print("-" * 40)
