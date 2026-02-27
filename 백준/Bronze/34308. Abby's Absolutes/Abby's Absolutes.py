import sys

it = iter(sys.stdin.read().split())
N = int(next(it)); K = int(next(it))
mid = (N + 1) / 2
ans = []
for _ in range(K):
    x = int(next(it))
    ans.append(str(N if x > mid else 1))
print(" ".join(ans))