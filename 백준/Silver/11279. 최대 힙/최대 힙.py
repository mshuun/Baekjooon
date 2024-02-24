import sys
input=sys.stdin.readline
import heapq
n = int(input())
arr=[]
for i in range(n):
    x = int(input())
    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(-1*heapq.heappop(arr))
    else:
        heapq.heappush(arr,-1*x)