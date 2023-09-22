import sys
input=sys.stdin.readline
n=int(input())
l=sorted([tuple(map(int,input().split()))for _ in range(n)],key=lambda x:(x[1],x[0]))
e=c=0
for s,f in l:
    if s>=e:
        c+=1
        e=f
print(c)