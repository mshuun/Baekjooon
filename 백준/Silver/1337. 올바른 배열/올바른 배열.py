N = int(input())
l = [int(input()) for _ in range(N)]
l.sort()
r = 5
for i in range(N):
    for j in range(i, i+5):
        a = l[i:j+1][::-1]
        z = len(a)
        if sum(a[k]-a[k+1] for k in range(z-1)) < 5:
            r = min(r, 5-z)
print(r)
