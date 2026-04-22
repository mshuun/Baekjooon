for _ in range(3):
    a = input()
    if a.count('1') == 1:
        print('C')
    elif a.count('1') == 2:
        print('B')
    elif a.count('1') == 3:
        print('A')
    elif a.count('1') == 4:
        print('E')
    else:
        print('D')