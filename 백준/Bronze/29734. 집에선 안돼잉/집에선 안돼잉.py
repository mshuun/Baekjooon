N,M=map(int,input().split())
T,S=map(int,input().split())
h=N+(N//8-(N%8==0))*S
d=M+T+(M//8-(M%8==0))*(T+T+S)
print(('Dok','Zip')[h<d],min(h,d))
