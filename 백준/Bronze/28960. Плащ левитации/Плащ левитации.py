h, l, a, b = map(int, input().split())
h *= 2
if (h >= a and l >= b) or (h>=b and l>=a):
    print("YES")
else:
    print("NO")