def solution(clothes):
    d = {}
    for _, kind in clothes:
        d[kind] = d.get(kind, 1) + 1
    r = 1
    for n in d.values():
        r *= n
    return r - 1