from collections import deque, defaultdict

def bfs_shortest_reach(n, edges, start, weight):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    distances = [-1] * (n + 1)  # 1-indexed nodes
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    distances[start] = 0

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distances[neighbor] = distances[node] + weight
                queue.append(neighbor)

    # Return distances excluding the start node
    return [distances[i] for i in range(1, n + 1) if i != start]



n = 5
edges = [[1, 2], [1, 3], [3, 4]]
s = 1
w = 6

print(bfs_shortest_reach(n, edges, s, w))
## [6, 6, 12, -1]