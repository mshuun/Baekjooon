import sys
C = [0 for i in range(1001)]
D = -1
cc = 0
input = sys.stdin.readline
for _ in range(int(input())):
    d, c = input().split()
    c = int(c)
    if c > 1000:
        cc += 1
    else:
        if d == 'jinju':
            D = c
        if D == -1:
            C[c] += 1
        elif D < c:
            cc += 1
print(D)
print(cc+sum(C[D+1:]))
