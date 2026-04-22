s = int(input())
a = int(input())
r = (a - s) if s <= a else (24 - (s - a))
print(r)
