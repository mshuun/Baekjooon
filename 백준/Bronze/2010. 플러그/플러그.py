from sys import stdin
input = stdin.readline
n = int(input())
a = 0
for _ in range(n):
    a += int(input())
print(a-(n-1))