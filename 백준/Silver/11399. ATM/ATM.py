a = int(input())
b = list(map(int,input().split()))
b.sort()
c = list()
c.append(b[0])
for i in range(1,a):
    c.append(c[i-1] + b[i])
print(sum(c))