N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
B = [list(map(int, input().split())) for i in range(N)]
C = []
for i in range(N):
    a = []
    for j in range(M):
        a.append(A[i][j]+B[i][j])
    C.append(a)
for i in C:
    print(*i)