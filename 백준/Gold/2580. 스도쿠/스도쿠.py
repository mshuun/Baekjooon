import sys

board = [list(map(int, input().split())) for _ in range(9)]
empty_cells = []
row_check = [[0] * 10 for _ in range(9)]
col_check = [[0] * 10 for _ in range(9)]
box_check = [[0] * 10 for _ in range(9)]

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            empty_cells.append((i, j))
        else:
            num = board[i][j]
            box_idx = (i // 3) * 3 + (j // 3)
            row_check[i][num] = 1
            col_check[j][num] = 1
            box_check[box_idx][num] = 1

def sudoku(idx):
    if idx == len(empty_cells):
        for line in board:
            print(*line)
        sys.exit(0)

    r, c = empty_cells[idx]
    box_idx = (r // 3) * 3 + (c // 3)

    for num in range(1, 10):
        if not row_check[r][num] and not col_check[c][num] and not box_check[box_idx][num]:
            row_check[r][num] = col_check[c][num] = box_check[box_idx][num] = 1
            board[r][c] = num
            
            sudoku(idx + 1)
            
            row_check[r][num] = col_check[c][num] = box_check[box_idx][num] = 0
            board[r][c] = 0

sudoku(0)