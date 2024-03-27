import sys
input = sys.stdin.readline
h, m, s = map(int, input().split())
S = h*3600 + m*60 + s
q = int(input())
for _ in range(q):
    i = list(map(int, input().split()))
    if len(i) == 1:
        r = S
        h = r//3600
        h %= 24
        r %= 3600
        m = r//60
        r %= 60
        s = r
        print(h, m, s)
    else:
        T, c = i
        if T == 1:
            S += c
        else:
            S -= c
