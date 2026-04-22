c = 0
while True:
    c+=1
    a = list(map(int,input().split()))
    if a[0] == 0:
        break
    n = a[0]
    a = a[1:]
    print("Case %a: %.1f" %( c, a[(n + 1) // 2 - 1] if n % 2 else (a[n // 2 - 1] + a[(n // 2)]) / 2) )