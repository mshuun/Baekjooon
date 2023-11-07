from itertools import permutations as p
n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
for i in p(l, m):
    print(*i)
