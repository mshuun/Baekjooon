def solution(k, tangerine):
    tan = {}
    for i in tangerine:
        if i in tan:
            tan[i] += 1
        else:
            tan[i] = 1
    a = sorted([[tan[i],i] for i in tan],reverse=1)
    r = 0
    s = 0
    for i,j in a:
        if s >= k:
            break
        r += 1
        s += i
        
    return r