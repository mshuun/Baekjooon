a, b, c = map(int, input().split())
e, f, g = map(int, input().split())
l = 0
if e > a:
    l += e-a
if f > b:
    l += f-b
if g > c:
    l += g-c
print(l)