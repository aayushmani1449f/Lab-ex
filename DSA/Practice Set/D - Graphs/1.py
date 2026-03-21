def build_network(users, friendships):
    graph = {user: [] for user in users}
    for u, v in friendships:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def get_friends(graph, user):
    return graph.get(user, [])