def solution(a):
    book = {v: i for i, v in enumerate(a)}
    return sum(p[:i] in book for p in a for i in range(len(p)))==0