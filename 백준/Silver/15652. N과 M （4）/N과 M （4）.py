from itertools import combinations_with_replacement as c
n, m = map(int, input().split())
for i in c(range(1, n+1), m):
    print(*i)
