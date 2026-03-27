import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return
    parent[rb] = ra
sc = 1
for _ in range(int(input())):
    print(f"Scenario {sc}:")
    sc+=1
    n = int(input())
    parent = list(range(n))
    for _ in range(int(input())):
        a, b = map(int, input().split())
        union(a, b)
    for _ in range(int(input())):
        a, b = map(int, input().split())
        print("1" if find(a) == find(b) else "0")
    print()