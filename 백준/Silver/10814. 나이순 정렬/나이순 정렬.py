import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
d = {}
for _ in range(n):
    o,w = input().split()
    o = int(o)
    d.setdefault(o, []).append(w)

for i in range(1,201):
    if i in d:
        for j in d[i]:
            print(str(i)+' '+j+'\n')