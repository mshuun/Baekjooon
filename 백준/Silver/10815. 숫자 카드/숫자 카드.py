import sys
input = sys.stdin.readline
n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
r = []
for i in b:
    if i in a:
        r.append(1)
    else:
        r.append(0)
print(*r)