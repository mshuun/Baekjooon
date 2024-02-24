import sys
input=sys.stdin.readline
import heapq
n = int(input())
pos=[]
neg=[]
for i in range(n):
    x = int(input())
    if x == 0:
        if len(pos) == 0 and len(neg) == 0:
            print(0)
        elif len(neg) == 0:
            print(heapq.heappop(pos))
        elif len(pos) == 0:
            print(-1*heapq.heappop(neg))
        else:
            nn = heapq.heappop(neg)
            pp = heapq.heappop(pos)
            if nn<=pp:
                print(-1*nn)
                heapq.heappush(pos,pp)
            elif pp<nn:
                print(pp)
                heapq.heappush(neg,nn)

    elif x>0:
        heapq.heappush(pos,x)
    else:
        heapq.heappush(neg,-1*x)