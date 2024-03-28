N = int(input())
A = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a-b)
A.sort()
if N % 2:
    print(1)
else:
    print(A[N//2]-A[N//2-1]+1)
