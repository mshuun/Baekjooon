import sys

n, m = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(n)]

max_side = 1

for i in range(n):
    for j in range(m):
        for k in range(1, min(n - i, m - j)):
            target = board[i][j]
            if (board[i][j+k] == target and 
                board[i+k][j] == target and 
                board[i+k][j+k] == target):
                if k + 1 > max_side:
                    max_side = k + 1

print(max_side ** 2)