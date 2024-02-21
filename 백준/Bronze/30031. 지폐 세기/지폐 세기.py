n = int(input())
s = 0
for i in range(n):
    g,_ = map(int,input().split())
    s += {136:1000,142:5000,148:10000,154:50000}[g]
print(s)