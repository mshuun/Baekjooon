N, M = map(int, input().split())
a = list(map(int, input().split()))
r = 1
for i in a:
    r *= i % M
    r %= M
print(r)
