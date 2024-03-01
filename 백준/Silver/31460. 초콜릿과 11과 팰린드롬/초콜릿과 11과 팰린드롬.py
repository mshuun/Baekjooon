for _ in range(int(input())):
    n = int(input())
    if n<4:
        print([0,11,858][n-1])
    elif n%2==0:print('1'*n)
    else:print('11'+'0'*(n-4)+'11')