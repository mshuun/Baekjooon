import heapq
n = int(input())
a = []
for i in range(n):
    for j in map(int,input().split()):
        if len(a)<n:
            heapq.heappush(a,j)
        elif a[0] < j:
            heapq.heappop(a)
            heapq.heappush(a,j)
print(a[0])