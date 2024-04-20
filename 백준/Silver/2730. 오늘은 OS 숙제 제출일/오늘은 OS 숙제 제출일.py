from datetime import *
T = int(input())
for _ in range(T):
    a, b = input().split()
    M, D, Y = map(int, a.split('/'))
    m, d = map(int, b.split('/'))
    A = datetime(Y, M, D, 0, 0, 0)
    B = datetime(Y, m, d, 0, 0, 0)
    try:
        C = datetime(Y-1, m, d, 0, 0, 0)
    except:
        C = B
    try:
        D = datetime(Y+1, m, d, 0, 0, 0)
    except:
        D = B
    E = [(B-A).days, (C-A).days, (D-A).days]
    mm = min([abs(i) for i in E])
    day = [i for i in E if abs(i) == mm][0]
    date = A+timedelta(days=day)
    if day == 0:
        print("SAME DAY")
    elif mm > 7:
        print("OUT OF RANGE")
    else:
        S = "S" if mm != 1 else ""
        AP = "AFTER" if day > 0 else "PRIOR"
        print(f"{date.month}/{date.day}/{date.year} IS {mm} DAY{S} {AP}")
