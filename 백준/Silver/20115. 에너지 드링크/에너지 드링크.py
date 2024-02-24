n = int(input())
x = list(map(int, input().split()))
m = max(x)
print(m+(sum(x)-m)/2)