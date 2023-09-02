import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
A = [int(input()) for _ in range(n)]
A.sort()
for i in A:print(str(i)+'\n')