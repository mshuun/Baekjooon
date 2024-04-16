a,b=map(int,input().split())
D=abs(b-a)
if a!=b:
 while D%2==0:D//=2
 a,b=(1,1+D)if a<b else(1+D,1)
while 1:
 try:x,y=map(int,input().split());d=abs(y-x);print('Y'if(a<=b)==(x<=y)and(D==d or d and D and d%D==0)else'N')
 except:break
