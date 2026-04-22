import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l,r,n,m = map(int,input().split())
    d = abs(m - n)
    if n == m:
        print("G")
    elif l >= d and r >= d:
        print("E") 
    elif l>=d :
        print("L")
    elif r>=d :
        print("R")
    else:
        print("E")