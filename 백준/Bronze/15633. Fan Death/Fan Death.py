n=int(input())
print(sum(i for i in range(1,n+1) if n%i==0)*5-24)