n = int(input())
if n >= 1000000:
    r = 0.2
elif n >= 500000:
    r = 0.15
elif n >= 100000:
    r = 0.1
else:
    r = 0.05

print(int(n * r), int(n * (1 - r)))
