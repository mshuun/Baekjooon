x,y = map(int,input().split())
n = int(input())
prices= []
for _ in range(n):
    i,j=map(float,input().split())
    prices.append(i/j*1000)
print(round(min(min(prices),x/y*1000),2))