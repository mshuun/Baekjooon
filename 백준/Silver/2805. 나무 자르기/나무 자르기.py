import bisect
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()

prefix = [0] * (N + 1)
for i in range(N):
    prefix[i+1] = prefix[i] + tree[i]

r = 0
a = 0
b = tree[-1]

while a <= b:
    c = (a + b) // 2

    idx = bisect.bisect_right(tree, c)
    
    count = N - idx
    take = (prefix[N] - prefix[idx]) - (count * c)
    
    if take < M:
        b = c - 1
    else:
        a = c + 1
        r = c
        
print(r)