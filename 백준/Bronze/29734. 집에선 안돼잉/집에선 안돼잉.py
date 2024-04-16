N, M = map(int, input().split())
T, S = map(int, input().split())

home = N + (N//8 - (N % 8 == 0))*S
dok = M + T + (M//8 - (M % 8 == 0))*(T+T+S)

if home < dok:
    print('Zip')
    print(home)
else:
    print('Dok')
    print(dok)
