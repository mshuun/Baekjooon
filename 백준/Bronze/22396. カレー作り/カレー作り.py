while 1:
    r0,w0,c,r=map(int,input().split())
    if r0 == 0 and w0 == 0 and c == 0 and r == 0:
        break
    r1 = c*w0-r0
    print(max(0,r1//r+(r1%r!=0)))