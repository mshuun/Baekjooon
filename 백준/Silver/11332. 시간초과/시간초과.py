from math import factorial as f
C = int(input())
for _ in range(C):
    S, N, T, L = input().split()
    N, T, L = map(int, [N, T, L])
    if S == 'O(N)':
        t = N
    elif S == 'O(N^2)':
        t = N*N
    elif S == 'O(N^3)':
        t = N*N*N
    elif S == 'O(2^N)':
        t = 2**N
    else:
        if N > 12:
            print("TLE!")
            continue
        t = f(N)
    if t*T <= 10**8*L:
        print("May Pass.")
    else:
        print("TLE!")