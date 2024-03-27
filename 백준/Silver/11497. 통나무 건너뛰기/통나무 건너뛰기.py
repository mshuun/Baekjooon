T = int(input())
for i in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    l = L[::2]
    r = L[1::2]
    r = r[::-1]
    L = l+r
    m = 0
    for j in range(len(L)):
        m = max(m, abs(L[j]-L[j-1]))
    print(m)
