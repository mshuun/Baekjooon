n = int(input())
l = list()
for i in range(n):
    a, b, c = map(int, input().split())
    k = [a, b, c]
    if a == b and b == c:
        l.append(10000+a*1000)
    elif a == b or a == c:
        l.append(1000+a*100)
    elif b == c:
        l.append(1000+b*100)
    else:
        l.append(max(k)*100)
print(max(l))
