print('none'if sum(S:=[*map(int,input().split())])<100 else next(('hacker'for i,v in enumerate(S)if v>(i//2+1)*100),'draw'))