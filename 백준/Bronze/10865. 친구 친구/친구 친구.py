import sys
input = sys.stdin.readline
N,M=map(int,input().split())
f=[0 for _ in range(N)]
for _ in range(M):
    a,b=map(int,input().split())
    f[a-1]+=1
    f[b-1]+=1
print(*f)