M = int(input())
N = int(input())
sosoo = list()
for i in range(M,N+1):
    cnt = 0
    for j in range(1,int(i ** (1/2)+1)):
        if i%j == 0 :
            cnt += 1
        if cnt == 2 :
            break
    if cnt == 1 and i != 1:
        sosoo.append(i)
if len(sosoo) == 0 :
    print(-1)
else :
    print(sum(sosoo))
    print(sosoo[0])