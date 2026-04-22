while True:
    a = list(input())
    if a == list('0'):
        break
    b = a.copy()
    a.reverse()
    if a == b :
        print('yes')
    else:
        print('no')