N, M = map(int, input().split())
matrix = []
for i in range(3 * N):
    matrix.append(input())

grid = [list(row) for row in matrix]

for i in range(N):
    for j in range(M):
        equ = ''.join(grid[i*3+1][j*8+1:j*8+7]).replace('.', '')
        leng = len(equ)
        a, b_c = equ.split('+')
        b, c = b_c.split('=')
        if int(a) + int(b) == int(c):
            for x in range(i*3+1, i*3+2):
                for y in range(j*8, j*8+7):
                    if grid[x][y] == '.':
                        grid[x][y] = '*'
                if grid[x][j*8+6] != '*':
                        grid[x][j*8+7] = '*'

            for y in range(j*8+1, j*8+1+leng):
                if grid[i*3][y] == '.':
                    grid[i*3][y] = '*'
                if grid[i*3+2][y] == '.':
                    grid[i*3+2][y] = '*'
        else:
            grid[i*3+2][j*8+1] = '/'
            grid[i*3+1][j*8+2] = '/'
            grid[i*3][j*8+3] = '/'

result = [''.join(row) for row in grid]
for i in result:
    print(*i, sep='')