import sys
input=sys.stdin.readline
import heapq
heapq.heapify(d:=[int(input()) for _ in range(int(input()))])
print(sum(heapq.heappush(d,(a:=heapq.heappop(d))+(b:=heapq.heappop(d))) or a+b for _ in range(len(d)-1)))