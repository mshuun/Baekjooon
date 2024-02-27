for _ in range(int(input())):
    a,A,b,B,c,C=map(int, input().split())
    d=((B-a)**2+(c-A)**2)**0.5
    if d==0 and b==C:
        print(-1)
    elif d==b+C or d==abs(b-C):
        print(1)
    elif abs(b-C)<d<(b+C):
        print(2)
    else:
        print(0)
