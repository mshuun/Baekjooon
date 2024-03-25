N = int(input())
result = 0
for i in range(N):
    num = int(input())
    a, b = divmod(num, 10)
    result += a**b

print(result)
