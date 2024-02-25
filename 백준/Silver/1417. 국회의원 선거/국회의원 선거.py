import heapq
arr=[]
c = 0
n = int(input())
n1 = int(input())
arr = [-int(input()) for _ in range(n - 1)]
heapq.heapify(arr)
while arr:
    a = -heapq.heappop(arr)
    if a >= n1+c:
        c+=1
        heapq.heappush(arr,-(a-1))
print(c)