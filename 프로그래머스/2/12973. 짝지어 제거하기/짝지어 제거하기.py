def solution(s):
    a = []
    for i in s:
        if len(a) == 0 or a[-1] != i :
            a.append(i)
        else:
            a.pop()
    return int(len(a) == 0)