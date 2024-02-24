import sys
import heapq
input = sys.stdin.readline
decks = []
for i in range(int(input())):
    heapq.heappush(decks,int(input()))
n = 0
while len(decks)>1:
    a = heapq.heappop(decks) + heapq.heappop(decks)
    n += a
    heapq.heappush(decks,a)
print(n)
