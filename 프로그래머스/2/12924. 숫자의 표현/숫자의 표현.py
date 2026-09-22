def solution(n):
    answer = 0
    left, right = 1, 1
    s = 1

    while left < n:
        if s < n:
            right += 1
            s += right
        elif s > n:
            s -= left
            left += 1
        else:
            answer += 1
            s -= left
            left += 1
            
    return answer + 1