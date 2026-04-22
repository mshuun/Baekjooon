n = int(input())
x = int(input())
s = list(map(int, input().split()))

o = [p for p in s if p > 0]
e = [p for p in s if p < 0]

mc = sum(p**x for p in o)

if x % 2 == 0:
    mc += sum(abs(p)**x for p in e)

print(mc)
