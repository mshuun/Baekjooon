def solution(a):
    n = 0
    for i in a:
        if i in '0123456789':
            n += int(i)
    return n