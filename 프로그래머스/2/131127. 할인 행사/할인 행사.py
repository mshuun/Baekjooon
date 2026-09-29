def solution(want, number, discount):
    wa = [[i,j] for i,j in zip(want,number)]
    re = 0
    for i in range(len(discount)-9):
        disc = discount[i:i+10]
        f = 0
        for a,b in wa:
             if disc.count(a) != b:
                    f = 1
                    break
        if f == 0:
            re += 1
    return re