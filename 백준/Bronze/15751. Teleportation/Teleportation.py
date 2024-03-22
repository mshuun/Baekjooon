a, b, x, y = map(int, input().split())
if a > b:
    a, b = b, a
if x > y:
    x, y = y, x
print(min(max(a, x)-min(a, x)+max(b, y)-min(b, y), b-a))
