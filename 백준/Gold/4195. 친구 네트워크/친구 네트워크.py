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
    
    if ra != rb:
        parent[rb] = ra
        count[ra] += count[rb]

for _ in range(int(input())):
    n = int(input())
    parent = []
    count = []
    nameidx = {}
    idx = 0
    
    for _ in range(n):
        a, b = input().split()
        for name in [a, b]:
            if name not in nameidx:
                nameidx[name] = idx
                parent.append(idx)
                count.append(1)
                idx += 1
                
        union(nameidx[a], nameidx[b])
        
        print(count[find(nameidx[a])])