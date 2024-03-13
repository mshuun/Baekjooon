h, m = map(int, input().split(':'))
n = int(input())
if m == 0:
    n -= h
elif m in [15,30,45]:
    n -= 1
elif m<15:
    m = 15
    n -= 1
elif m<30:
    m = 30
    n -= 1
elif m<45:
    m = 45
    n -= 1
else:
    m = 0
    h += 1
    n -= h
while 1:
    if n<1:
        break
    m += 15
    if m == 60:
        m = 0
        h += 1
        if h>12:
            h -= 12
        n -= h
    else:
        n -= 1
    
print(f"{h:02d}:{m:02d}")