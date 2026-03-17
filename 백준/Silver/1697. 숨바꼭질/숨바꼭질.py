from collections import deque

n, k = map(int, input().split())
visi = [False for _ in range(100001)]


def bfs(st):
    visi[st] = True
    sec = 0
    q = deque([[st, sec]])

    while q:
        s, sec = q.popleft()
        didi = [s - 1, s + 1, 2 * s]
        if s == k:
            return sec

        for di in didi:
            if 0 <= di <= 100000 and visi[di] == False:
                visi[di] = True
                q.append([di, sec + 1])


print(bfs(n))
