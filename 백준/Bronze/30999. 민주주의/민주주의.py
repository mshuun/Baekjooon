N, M = map(int, input().split())

c = 0

for i in range(N):
    o = input()
    if o.count('O') > M // 2:
        c += 1

print(c)
