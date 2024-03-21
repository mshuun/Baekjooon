N, a, b = map(int, input().split())
C = [[*map(int, input().split())]for i in range(N)]
a -= 1
b -= 1
angry = 0
jinseo = C[a][b]
for i, c in enumerate(C):
    for j, z in enumerate(c):
        if (i == a or j == b) and z > jinseo:
            angry = 1

if angry:
    print('ANGRY')
else:
    print('HAPPY')
