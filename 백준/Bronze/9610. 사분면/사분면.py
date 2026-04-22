n = int(input())
w = [0, 0, 0, 0, 0]
for i in range(n):
    a, b = map(int, input().split())
    if a == 0 or b == 0:
        w[4] += 1
    elif a > 0 and b > 0:
        w[0] += 1
    elif a < 0 and b > 0:
        w[1] += 1
    elif a < 0 and b < 0:
        w[2] += 1
    elif a > 0 and b < 0:
        w[3] += 1

print(f'Q1: {w[0]}')
print(f'Q2: {w[1]}')
print(f'Q3: {w[2]}')
print(f'Q4: {w[3]}')
print(f'AXIS: {w[4]}')
