a, b, c = map(int, input().split())
d, e, f = map(int, input().split())

d = -(-d // 100)
e = -(-e // 50)
f = -(-f // 20)
print(a * d + b * e + c * f)
