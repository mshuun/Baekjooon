import sys
input = sys.stdin.readline
print = sys.stdout.write
n,m=map(int,input().split())
nums=list(map(int,input().split()))
pre=[0]
for num in nums:
    pre.append(pre[-1]+num)
for i in range(m):
    i,j=map(int,input().split())
    print(str(pre[j]-pre[i-1])+'\n')