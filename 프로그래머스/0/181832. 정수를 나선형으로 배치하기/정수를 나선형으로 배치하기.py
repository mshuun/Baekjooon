def solution(n):
    c = n//2 + n%2
    answer = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 1
    for i in range(c):
        for j in range(i, n - i):
            answer[i][j] = cnt
            cnt += 1
        for j in range(i+1, n - i):
            answer[j][n - i - 1] = cnt
            cnt += 1
        for j in range(n - i - 2, i - 1, -1):
            answer[n - i - 1][j] = cnt
            cnt += 1
        for j in range(n - i - 2, i , -1):
            answer[j][i] = cnt
            cnt += 1
    return answer