def solution(genres, plays):
    d = {}
    s = {}
    for n,i in enumerate(zip(genres,plays)):
        gen, play = i
        d[gen] = d.get(gen,[]) + [[play,-n]]
        s[gen] = s.get(gen,0) + play
    s = sorted([[j,i] for i,j in s.items()],reverse = 1)
    result = []
    
    for i,j in s:
        d[j].sort(reverse=1)
        result.append(-d[j][0][1])
        if len(d[j])>1:
            result.append(-d[j][1][1])
        
    return result
