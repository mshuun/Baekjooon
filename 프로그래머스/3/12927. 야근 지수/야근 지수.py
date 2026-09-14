import heapq

def solution(n, works):
    h = [(-i,i) for i in works]
    
    heapq.heapify(h)
    
    for i in range(n):
        a = heapq.heappop(h)
        heapq.heappush(h,(a[0]+1, a[1]-1))
    
    a = sum(max(0,i[1])**2 for i in h)
    
    return a