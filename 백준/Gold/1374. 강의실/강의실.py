import heapq as h
import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[1])  

rooms = [arr[0][2]] 

for i in range(1, n):
    num, start, end = arr[i]
    if start >= rooms[0]: 
        h.heappop(rooms) 
    h.heappush(rooms, end) 

print(len(rooms))
