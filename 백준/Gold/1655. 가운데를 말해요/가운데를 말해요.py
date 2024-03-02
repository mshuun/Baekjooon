from heapq import heappush as push,heappop as pop
import sys
input = sys.stdin.readline
L = []
R = []
for i in range(int(input())):
    n = int(input())
    if len(L) == len(R): push(L, -n)
    else: push(R, n)
    if R and R[0] < -L[0]:
        l = pop(L)
        r = pop(R)
        push(L, -r)
        push(R, -l)
    print(-L[0])