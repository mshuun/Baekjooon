def solution(numbers):
    a = []
    b = [-1]*len(numbers)
    for i,n in enumerate(numbers):
        if len(a) == 0 or a[-1][0] >= n:
            a.append((n,i))
        else:
            while len(a) != 0 and a[-1][0] < n:
                b[a[-1][1]] = n
                a.pop()
            a.append((n,i))
    return b