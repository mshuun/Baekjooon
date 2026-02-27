import bisect
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
tree = list(map(int,input().split()))
tree.sort()

r = 0
a = 0
b = 1000000000
while a <= b:
    c = (a+b)//2
    take = 0
    idx = bisect.bisect_right(tree, c)
    
    for i in tree[idx:]:
        if i>c:
            take += i-c
    if take<M:
        b = c - 1
    elif take>=M:
        a = c + 1
        r = c
    
print(r)