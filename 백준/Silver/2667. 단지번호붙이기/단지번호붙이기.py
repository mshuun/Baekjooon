def dfs(graph, start, visited):
    visited[start] = True
    dfs_list.append(start)
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)


N = int(input())
graph = [[] for _ in range(N*N+1)]
maps = []
connection = []
for i in range(N):
    maps.append(input())
for i in range(N):
    for j in range(N):
        if maps[i][j] == '1':
            location = N*i+j+1
            val = maps[i][j]
            connection.append((location, location))
            if i != 0:
                if maps[i-1][j] == '1':
                    connect = (location, N*(i-1)+j+1)
                    if connect not in connection:
                        connection.append(connect)
            if i != N-1:
                if maps[i+1][j] == '1':
                    connect = (location, N*(i+1)+j+1)
                    if connect not in connection:
                        connection.append(connect)
            if j != 0:
                if maps[i][j-1] == '1':
                    connect = (location, N*i+j)
                    if connect not in connection:
                        connection.append(connect)
            if j != N-1:
                if maps[i][j+1] == '1':
                    connect = (location, N*i+j+2)
                    if connect not in connection:
                        connection.append(connect)
for i in connection:
    a, b = i
    graph[a].append(b)
result = []
for i in range(N*N+1):
    if graph[i] != []:
        dfs_list = []
        visited = [False for _ in range(N*N+1)]
        dfs(graph, i, visited)
        dfs_list.sort()
        if dfs_list not in result:
            result.append(dfs_list)
print(len(result))
a = []
for i in result:
    a.append(len(i))
a.sort()
for i in a:
    print(i)
