for _ in range(int(input())):
    n,a,b = map(int,input().split())
    if a>b:
        a,b=b,a
    h = list(map(int,input().split()))
    L,M,R=[],[],[]
    mid = (a+b)/2
    for i in h:
        if i<mid:
            L.append(i)
        elif i>mid:
            R.append(i)
        else:
            M.append(i)
    a_mov = sum(L) - len(L) * a
    b_mov = len(R) * b - sum(R)
    for i in M:
        if a_mov < b_mov:
            a_mov += i - a
        else:
            b_mov += b - i
    total =  (a_mov + b_mov)*2
    print(total,2*abs(a_mov - b_mov))