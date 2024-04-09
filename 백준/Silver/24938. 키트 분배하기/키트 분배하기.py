N = int(input())
a = list(map(int, input().split()))
T = sum(a) // N
r = 0

for i in range(N-1):
    t = T - a[i]
    r += abs(t)
    a[i+1] -= t

print(r)
