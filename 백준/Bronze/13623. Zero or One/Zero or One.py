a, b, c = input().split()
if a == b != c:
    print('C')
elif a == c != b:
    print('B')
elif b == c != a:
    print('A')
else:
    print('*')
