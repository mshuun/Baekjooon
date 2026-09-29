def solution(n, words):
    w = {words[0]:0}
    if len(words[0]) == 1:
        return [1,1]
    for i in range(1,len(words)):
        a = words[i-1]
        b = words[i]
        if a[-1] != b[0] or len(b) == 1 or b in w:
            return [i%n+1,i//n+1]
        else:
            w[b] = 0

    return [0,0]