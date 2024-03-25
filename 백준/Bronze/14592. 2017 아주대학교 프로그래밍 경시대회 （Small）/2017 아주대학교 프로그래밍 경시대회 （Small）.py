N=int(input())
S=[]
for i in range(N):
 s,c,l=map(int,input().split())
 S.append([-s,c,l,i])
print(sorted(S)[0][3]+1)
