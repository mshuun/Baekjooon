def solution(a, b):
    if len(b) > len(a):
        a,b=b,a
        
        
    a = list(map(int,list(a)[::-1]))
    b = list(map(int,list(b)[::-1]))
    while len(a) != len(b):
        b.append(0)
    
    for i in range(len(b)):
        c = a[i] + b[i]
        if c>9:
            if i == len(b) - 1:
                a.append(1)
            else:
                a[i+1] += 1
        a[i] = c%10
        
    a = a[::-1]
    
        
    a = list(map(str,a))
    return ''.join(a)