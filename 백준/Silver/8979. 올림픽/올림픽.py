N,K = map(int,input().split())
score = sorted([[i[1]*100+i[2]*10+i[3],i[0]] for i in [list(map(int,input().split())) for _ in range(N)]],reverse=1)
print(sum([1 for i in score if i[0]>sum([i[0] for i in score if i[1]==K])])+1)