import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [i for i in range(1,N+1)]
for _ in range(M):
    i,j = map(int,input().split())
    arr2 = arr[i-1:j]
    arr = arr[:i-1] + arr2[::-1] + arr[j:]

print(*arr)
