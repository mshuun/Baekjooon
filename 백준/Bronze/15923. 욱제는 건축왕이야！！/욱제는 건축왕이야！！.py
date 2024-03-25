a, b = [], []
N = int(input())
for i in range(N):
    c, d = map(int, input().split())
    a.append(c)
    b.append(d)
print((max(a)+max(b)-min(b)-min(a))*2)
