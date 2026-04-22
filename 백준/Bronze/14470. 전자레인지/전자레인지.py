a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
t = 0
if a < 0:
    if b < 0:
        t += (b-a)*c
    else:
        t += (0-a)*c
        t += d
        t += b*e
else:
    t += (b-a)*e
print(t)