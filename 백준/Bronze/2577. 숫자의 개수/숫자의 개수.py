a = int(input())
b = int(input())
c = int(input())
l = list(map(int,str(a*b*c)))
for i in range(10) :
    cnt = 0
    for j in range(len(l)):
        if i == l[j] :
            cnt += 1
    print(cnt)