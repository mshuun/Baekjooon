a = input()
s = 0 
h = ''  
b = True  
for i in a:
    if i == 'X':
        s += 1
    else:
        if s % 2 == 1:
            b = False
            break
        h += 'A' * (s // 4 * 4)
        s %= 4 
        h += 'B' * (s // 2 * 2)
        s = 0
        h += '.'

if s % 2 == 1:
    b = False
else:
    h += 'A' * (s // 4 * 4)
    s %= 4
    h += 'B' * (s // 2 * 2)
    
if b:
    print(h)
else:
    print(-1)
