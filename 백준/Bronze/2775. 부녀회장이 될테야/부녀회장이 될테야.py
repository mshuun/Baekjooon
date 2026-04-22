n = int(input())
for i in range(n):
    l=list(range(1,15))
    a=int(input())
    b=int(input())
    nl=l
    for j in range(0,a):
        nl=[]
        for k in range(14):
            nl.append(sum(l[0:k+1]))
        l = nl
    print(nl[b-1])