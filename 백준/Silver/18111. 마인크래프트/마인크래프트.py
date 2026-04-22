import sys
N, M, B = map(int,input().split())
b = []
for _ in range(N):
    b.append([int(x) for x in sys.stdin.readline().rstrip().split()])

ans = int(1e9)
g = 0

for i in range(257): 
    use_b = 0
    take_b = 0
    for x in range(N):
        for y in range(M):
            if b[x][y] > i:
                take_b += b[x][y] - i
            else:
                use_b += i - b[x][y]

    if use_b > take_b + B:
        continue

    count = take_b * 2 + use_b

    if count <= ans:
        ans = count
        g = i

print(ans, g)