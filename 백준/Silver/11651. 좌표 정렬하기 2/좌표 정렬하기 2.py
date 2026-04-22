n = int(input())
l = list()
for i in range(n):
    a, b = map(int, input().split())
    l.append([a, b])
l.sort(key=lambda x: (x[1], x[0]))
for i in range(len(l)):
    print(*l[i])
