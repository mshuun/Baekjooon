n, m = map(int, input().split())
listA = [list(map(int, list(input()))) for _ in range(n)]
listB = [list(map(int, list(input()))) for _ in range(n)]


def check(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            listA[x][y] = 1 - listA[x][y]


cnt = -1 if (n < 3 or m < 3) and listA != listB else 0
for r in range(n-2):
    for c in range(m-2):
        if listA[r][c] != listB[r][c]:
            cnt += 1
            check(r, c)

if cnt != -1 and listA != listB:
    cnt = -1

print(cnt)
