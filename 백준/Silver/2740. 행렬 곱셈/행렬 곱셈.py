n, m  = map(int,input().split())
A = []
B = []
for i in range(n):
    A.append(list(map(int,input().split())))
m, k = map(int,input().split())
for i in range(m):
    B.append(list(map(int,input().split())))

C = []
for i in range(n):
    t = []
    for j in range(k):
        
        tt = 0
        for l in range(m):
            tt += A[i][l]*B[l][j]
        t.append(tt)
    C.append(t)
for i in C:
    print(*i)