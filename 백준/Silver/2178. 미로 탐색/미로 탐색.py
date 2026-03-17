from collections import deque

n, m = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(sr, sc):
    queue = deque([(sr, sc, 1)])
    visited[sr][sc] = True

    while queue:
        r, c, d = queue.popleft()

        if r == n - 1 and c == m - 1:
            return d

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if miro[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc, d + 1))


print(bfs(0, 0))
