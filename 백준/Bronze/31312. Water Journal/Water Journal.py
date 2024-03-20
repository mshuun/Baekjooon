n, a, b = map(int, input().split())
log = []
for i in range(n-1):
    w = int(input())
    log.append(w)
if max(log) != b and min(log) != a:
    print(-1)
elif max(log) != b:
    print(b)
elif min(log) != a:
    print(a)
else:
    for i in range(a, b+1):
        print(i)
