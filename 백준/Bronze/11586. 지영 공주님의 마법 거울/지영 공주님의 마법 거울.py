N = int(input())
mirror = [input() for _ in range(N)]
K = int(input())

if K == 1:
    for row in mirror:
        print(row)
elif K == 2:
    for row in mirror:
        print(row[::-1])
else:
    for row in mirror[::-1]:
        print(row)
