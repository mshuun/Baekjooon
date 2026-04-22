import sys
input = sys.stdin.readline

N = int(input())
a = [int(input()) for _ in range(N)]
a.sort(reverse=True)
print(*a, sep='\n')