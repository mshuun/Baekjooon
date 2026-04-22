k = int(input())
n = int(input())
p = k
b = 0
r = 0
for _ in range(n):
    t,z = input().split()
    t = int(t)
    b += t
    if b>210 and r == 0:
        r = p
    if z == 'T':
        p += 1
    if p>8:
        p = 1
print(r)