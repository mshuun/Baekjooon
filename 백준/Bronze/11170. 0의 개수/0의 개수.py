t = int(input())
for i in range(t):
    c = 0
    n, m = map(int, input().split())
    for j in range(n, m+1):
        c += str(j).count('0')
    print(c)