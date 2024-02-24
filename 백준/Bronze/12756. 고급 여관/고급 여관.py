a,b=map(int,input().split())
c,d=map(int,input().split())
A=d//a if d%a==0 else d//a+1
B=b//c if b%c==0 else b//c+1
if A<B:
    print("PLAYER A")
elif A>B:
    print("PLAYER B")
else:
    print("DRAW")