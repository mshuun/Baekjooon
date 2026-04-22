import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N + 1)]
parent_of = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

queue = deque([1])

while queue:
    node = queue.popleft()
    for child in tree[node]:
        if parent_of[child] == 0:
            parent_of[child] = node
            queue.append(child)

for i in range(2, N + 1):
    print(parent_of[i])
