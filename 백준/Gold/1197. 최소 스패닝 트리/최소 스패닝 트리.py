import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V,E = map(int,input().split())
edges = []
for _ in range(E):
    a,b,cost = map(int,input().split())
    edges.append([cost,a,b])
edges.sort()
parent = list(range(V+1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    c = find(a)
    d = find(b)
    if c == d:
        return
    parent[d] = c
t = 0
for edge in edges:
    cost,a,b = edge

    if find(a) != find(b):
        union(a,b)
        t += cost
print(t)