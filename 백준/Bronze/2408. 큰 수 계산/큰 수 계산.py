s = []
for i in range(int(input())*2-1):
    a = input()
    if a == '/':
        a = '//'
    s.append(a)
r = ''
for i in s:
    r += i
exec(f'print({r})')