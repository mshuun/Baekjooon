from collections import deque


def dfs(graph, start, visited):
    visited[start] = True
    dfs_list.append(start)
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        current = queue.popleft()
        bfs_list.append(current)
        for neighbor in graph[current]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True


dfs_list = []
bfs_list = []
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()
visited = [False for _ in range(n+1)]
dfs(graph, v, visited)
visited = [False for _ in range(n+1)]
bfs(graph, v, visited)
print(*dfs_list)
print(*bfs_list)
