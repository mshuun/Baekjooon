for i in range(int(input())):
    a = list(input())
    c = 0
    for j in range(len(a)):
        if a[j] == '(':
            c += 1
        else : c-=1
        if c < 0 :
            break
    if c == 0 :
        print('YES')
    else : print('NO')