def solution(land):
    n = len(land)
    m = len(land[0])

    xxxx = [0 for _ in range(m)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                land[i][j] = 0
                oil = 1
                oil_x = {j}
                stk = [(i, j)]

                while stk:
                    x, y = stk.pop()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m:
                            if land[nx][ny] == 1:
                                land[nx][ny] = 0
                                stk.append((nx, ny))
                                oil_x.add(ny)
                                oil += 1

                for col in oil_x:
                    xxxx[col] += oil

    return max(xxxx)