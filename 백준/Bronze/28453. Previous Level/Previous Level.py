N = int(input())
L = list(map(int, input().split()))

for x in L:
    if x >= 300:
        print(1, end=' ')
    elif x >= 275:
        print(2, end=' ')
    elif x >= 250:
        print(3, end=' ')
    else:
        print(4, end=' ')
