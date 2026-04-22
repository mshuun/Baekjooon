a = 0
b = 0
a += int(input())*3
a += int(input())*2
a += int(input())*1
b += int(input())*3
b += int(input())*2
b += int(input())*1
if b > a:
    print('B')
elif b < a:
    print('A')
else:
    print('T')