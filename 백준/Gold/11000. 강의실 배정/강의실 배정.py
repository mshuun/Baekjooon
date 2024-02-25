import heapq as h
import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort()
rooms = [arr[0][1]]

for i in range(1, n):
    start, end = arr[i]
    if start >= rooms[0]:
        h.heappop(rooms)
    h.heappush(rooms, end)

print(len(rooms))