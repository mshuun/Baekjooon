n = int(input())
cnt=0
for  i in range(n):
    a = list(input())
    l=[a[0]]
    for j in range(1,len(a)):
        if a[j] != a[j-1]:
            l.append(a[j])
    if len(set(a)) == len(l) :
        cnt += 1
print(cnt)