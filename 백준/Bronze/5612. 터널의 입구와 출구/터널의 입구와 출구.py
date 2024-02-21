n = int(input())
c = int(input())
m = c
zero = 0
for i in range(n):
    a,b = map(int, input().split())
    c = c + a - b
    if m < c:
        m = c
    if c < 0:
        zero = 1
if zero:
    print("0")
else:
    print(m)