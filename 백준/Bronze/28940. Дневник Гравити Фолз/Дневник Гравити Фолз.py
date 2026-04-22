w,h=map(int,input().split())
n,a,b=map(int,input().split())
if a>w or b>h:print(-1)
else:print((n+((w//a)*(h//b))-1)//((w//a)*(h//b)))