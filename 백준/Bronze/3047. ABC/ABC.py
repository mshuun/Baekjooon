a = list(map(int, input().split()))
a.sort()
a, b, c = a
s = input()
for i in s:
    if i == 'A':
        print(a, end=' ')
    elif i == 'B':
        print(b, end=' ')
    elif i == 'C':
        print(c, end=' ')