t = int(input())
for i in range(t):
    m = int(input())
    lst = list()
    for j in range((m-1)//10+1):
        lst.extend(list(map(int, input().split())))
    print(m//2+1)
    l = list()
    for j in range(0, m, 2):
        l.append(sorted(lst[0:j+1])[j//2])
    for j in range((m//2)//10+1):
        print(*l[10*j:10*(j+1)])
