from datetime import datetime as e,timedelta as t
for _ in range(int(input())):
    y,m = map(int, input().split())
    d = e(y,m,m)-t(m)
    print(d.year, d.month, d.day)