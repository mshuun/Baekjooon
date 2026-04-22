import sys
input = sys.stdin.readline

arr = [[0 for j in range(100)] for i in range(100)]
for _ in range(int(input())):
    x,y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j] = 1
c = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1: c+=1
print(c)