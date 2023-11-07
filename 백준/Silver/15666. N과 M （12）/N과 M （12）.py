from itertools import combinations_with_replacement as p
n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
for i in sorted(set(p(l, m))):
    print(*i)
