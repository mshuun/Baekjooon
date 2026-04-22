n = int(input())
for i in range(n):
    r, e, c = map(int, input().split())
    if e-r-c > 0:
        print('advertise')
    if e-r-c == 0:
        print('does not matter')
    if e-r-c < 0:
        print('do not advertise')
