import sys

sys.setrecursionlimit(10000)


def dfs(graph, start, visited):
    visited[start] = True
    dfs_list.append(start)
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)


T = int(input())
for _ in range(T):
    nears = []
    X, Y, K = map(int, input().split())
    maps = [[0 for _ in range(X)] for _ in range(Y)]
    for _ in range(K):
        x, y = map(int, input().split())
        maps[y][x] = 1
    for y in range(len(maps)):
        for x in range(len(maps[y])):
            if maps[y][x] == 1:
                nears.append([y*X+x, y*X+x])
                if x != 0:
                    if maps[y][x-1] == 1:
                        nears.append([y*X+x, y*X+x-1])
                if x != len(maps[y])-1:
                    if maps[y][x+1] == 1:
                        nears.append([y*X+x, y*X+x+1])
                if y != 0:
                    if maps[y-1][x] == 1:
                        nears.append([y*X+x, (y-1)*X+x])
                if y != len(maps)-1:
                    if maps[y+1][x] == 1:
                        nears.append([y*X+x, (y+1)*X+x])
    graph = [[] for _ in range(X*Y)]
    for i in nears:
        a, b = i
        graph[a].append(b)
    result = []
    for i in range(X*Y):
        if graph[i] != []:
            dfs_list = []
            visited = [False for _ in range(X*Y)]
            dfs(graph, i, visited)
            dfs_list.sort()
            if dfs_list not in result:
                result.append(dfs_list)
    print(len(result))
