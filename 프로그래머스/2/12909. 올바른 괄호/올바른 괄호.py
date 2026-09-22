def solution(s):
    answer = True
    op = 0
    
    for i in s:
        if i == '(':
            op += 1
        elif op == 0:
            answer = False
        else:
            op -= 1
    if op != 0:
        answer = False
    return answer