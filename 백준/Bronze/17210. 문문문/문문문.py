N = int(input())
f = int(input())
if N > 5:
    print('Love is open door')
else:
    if f:
        print(*[0, 1, 0, 1][:N-1])
    else:
        print(*[1, 0, 1, 0][:N-1])
