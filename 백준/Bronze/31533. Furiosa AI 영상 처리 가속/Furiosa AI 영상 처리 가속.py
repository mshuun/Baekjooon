a = int(input())
m, n = map(int, input().split())
r = min(m, n)/a
print(min(r*2, max(m, n)))
