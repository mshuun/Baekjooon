n,k = map(int,input().split())
import math
print(int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k))))