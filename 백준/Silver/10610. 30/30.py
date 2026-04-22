a = list(input())
if '0' not in a:
    print(-1)
else:
    s = 0
    for i in a:
        s += int(i)
    if s % 3 != 0:
        print(-1)
    else:
        a.sort(reverse=True)
        print(*a, sep='')