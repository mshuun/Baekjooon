while 1:
    s = input()
    if s == '.':
        break
    
    a = [-1]
    b = [-1]
    ll = len(s)
    r=1
    try:
        for i in range(ll):
            c = s[i]
            if c == '(':
                a.append(i)
            elif c == ')':
                if a[-1] < b[-1]:
                    r = 0
                if a[-1] != -1:
                    del a[-1]
                else:
                    r = 0
            elif c == '[':
                b.append(i)
            elif c == ']':
                if b[-1] < a[-1]:
                    r = 0
                if b[-1] != -1:
                    del b[-1]
                else:
                    r = 0
    except:
        r = 1

    if len(a)>1 or len(b)>1:
        r = 0
    if r:
        print("yes")
    else:
        print("no")