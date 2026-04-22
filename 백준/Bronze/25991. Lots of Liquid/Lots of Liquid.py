n = int(input())
a = list(map(float, input().split()))
b = 0
for i in a:
    b+=i**3
print(b**(1.0/3.0))