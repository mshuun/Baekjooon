T = int(input())
for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    L = L[::2] + L[1::2][::-1]
    m = max(abs(L[i] - L[i-1]) for i in range(N))
    print(m)