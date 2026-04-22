a, b = map(int, input().split())
if a % 2 == 1 and b % 2 == 1:
    print(min((a//2+1)*b-a//2*b, (b//2+1)*a-b//2*a))
else:
    print(0)