from itertools import permutations

n, m = map(int, input().split())
perms = permutations(range(1, n+1), m)

for perm in perms:
  print(" ".join(map(str, perm)))
