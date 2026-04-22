T = int(input())
for _ in range(T):
    input()
    N = int(input())
    candies = [int(input()) for _ in range(N)]
    if sum(candies) % N != 0:
        print('NO')
    else:
        print('YES')