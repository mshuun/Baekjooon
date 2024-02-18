n,u,l=map(int,input().split())
print('Very Good' if n>=1000 and (u>=8000 or l>=260) else 'Good' if n>=1000 else 'Bad')