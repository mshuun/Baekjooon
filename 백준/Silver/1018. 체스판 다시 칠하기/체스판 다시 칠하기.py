n, m = map(int, input().split())
chess_original = []

for i in range(n):
    chess_original.append(list(input()))


def check(chess):
    even = 0
    count_W = 0
    count_B = 0

    for i in range(8):
        for j in range(8):
            even += 1
            if even % 2 == 1:
                if chess[i][j] == 'B':
                    count_W += 1
            else:
                if chess[i][j] == 'W':
                    count_W += 1
        even += 1
    for i in range(8):
        for j in range(8):
            even += 1
            if even % 2 == 1:
                if chess[i][j] == 'W':
                    count_B += 1
            else:
                if chess[i][j] == 'B':
                    count_B += 1
        even += 1
    return min(count_W, count_B)


def slice(chess, x, y):
    chess_slice = []
    for i in range(y, y + 8):
        chess_slice.append(chess[i][x:x + 8])
    return chess_slice


def slice_and_check(chess, x, y):
    return check(slice(chess, x, y))


mins = []
for i in range(n-7):
    for j in range(m-7):
        mins.append(slice_and_check(chess_original, j, i))
print(min(mins))