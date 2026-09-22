def solution(s):
    answer = ''
    up = True
    for i in s:
        if up:
            answer += i.upper()
        else:
            answer += i.lower()
        if i == " ":
            up = True
        else:
            up = False
    return answer