def solution(a):
    for i in 'aeiou':
        a = a.replace(i,'')
    return a