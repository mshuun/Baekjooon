# BOJ 29752
# 최장 스트릭
n = int(input())
s = list(map(int,input().split()))
m = 0
c = 0
for i in range(n):
    if s[i] != 0:
        c += 1
    else:
        m = max(m,c)
        c = 0
m = max(m,c)
print(m)