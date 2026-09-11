from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n = len(maps)
    m = len(maps[0])
    
    if n == 1 and m == 1:
        return 1;
    
    dist = [[-1] * m for _ in range(n)]
    
    q = deque([(0,0)])
    dist[0][0] = 1
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                
                if maps[nx][ny] == 1 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
                    
                    if nx == n-1 and ny == m-1:
                        return dist[nx][ny]
                    
                    
    return -1