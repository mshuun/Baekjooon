a = int(input())
b = 0
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    b += x*y
if a == b:
    print('Yes')
else:
    print('No')
