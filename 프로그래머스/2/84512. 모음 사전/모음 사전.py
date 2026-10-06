def solution(word):
    z = "AEIOU "
    dd = []
    for a in z:
        for b in z:
            for c in z:
                for d in z:
                    for e in z:
                        f = a+b+c+d+e
                        k = ""
                        for g in f:
                            if g != " ":
                                k += g
                        dd.append(k)
    return sorted(set(dd)).index(word)