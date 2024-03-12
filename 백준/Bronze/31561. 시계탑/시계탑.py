m = int(input())
r = 0
if m >= 30:
    r += 15
    m -= 30
    r += m*1.5
else:
    r = m/2
print(r)