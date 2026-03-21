from collections import deque

def build_city_map(edges):
    graph = {}
    for u, v in edges:
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    return graph

def shortest_path(graph, start, end):
    queue = deque([[start]])
    visited = set([start])
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == end:
            return " -> ".join(path)
            
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
    return "No path"