A,B=map(int,input().split())
K,X=map(int,input().split())
r=max(0,min(B,K+X)-max(A,K-X)+1)
print(r if r else'IMPOSSIBLE')