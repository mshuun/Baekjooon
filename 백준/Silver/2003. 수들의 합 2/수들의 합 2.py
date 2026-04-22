n,m=map(int,input().split())
arr = list(map(int,input().split()))
pre = [0 for _ in range(n+1)]
for i in range(n):
    pre[i+1] = pre[i] + arr[i]
cnt = 0
left,right=0,1
while left<=n and right<=n:
    s = pre[right] - pre[left]
    if s == m:
        cnt +=1
        right +=1
    elif s < m :
        right +=1
    else:
        left +=1
print(cnt)