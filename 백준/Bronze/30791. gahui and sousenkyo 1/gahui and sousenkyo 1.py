v = list(map(int, input().split()))
r = v[0]
c = 0

for i in range(1, 5):
    if r - v[i] <= 1000:
        c += 1

print(c)
