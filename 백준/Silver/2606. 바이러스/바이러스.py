
def dfs(graph, start, visited):
    visited[start] = True
    dfs_list.append(start)
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)


dfs_list = []
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()
visited = [False for _ in range(n+1)]
dfs(graph, 1, visited)
print(len(dfs_list)-1)
