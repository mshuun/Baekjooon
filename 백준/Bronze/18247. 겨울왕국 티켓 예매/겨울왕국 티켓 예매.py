for _ in range(int(input())):
 a,b=map(int,input().split())
 if a<12 or b<4:print(-1)
 else:print(b*11+4)