import sys
input = sys.stdin.readline
n = int(input())
h = set()
for i in range(n):
    name, c = input().split()
    if c == 'enter':
        h.add(name)
    else:
        h.remove(name)
h = list(h)
h.sort(reverse=True)
print(*h)