k = int(input())
for i in range(k):
    y,x,n=map(int,input().split())
    l=[]
    for a in range(1,x+1) :
        for b in range(1,y+1):
            l.append(100*b+a)
    print(l[n-1])