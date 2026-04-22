a, b, c = map(int, input().split())
k = [a, b, c]
k.sort(reverse=True)
if a == b and b == c:
    print(10000+(a*1000))
elif a == b or a == c:
    print(1000+(a*100))
elif b == c:
    print(1000+(b*100))
else:
    print(k[0]*100)
