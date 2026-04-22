a, b = map(int, input().split())
c = list(map(int, input().split()))
print(*[i-a*b for i in c])