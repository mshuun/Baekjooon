import sys
input = sys.stdin.readline
while 1:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    A = []
    r = 0
    for i in range(n):
        A.append(int(input()))
    A = set(A)
    for i in range(m):
        if int(input()) in A:
            r += 1
    print(r)