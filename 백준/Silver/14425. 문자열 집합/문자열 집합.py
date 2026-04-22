import sys
input = sys.stdin.readline

r = 0
n,m = map(int,input().split())
s = [input() for _ in range(n)]
s = set(s)

for _ in range(m):
    if input() in s:
        r += 1
print(r)