n = int(input())

if n == 0:
    print(1)
elif n == 1:
    print(0)
else:
    result = "8" * (n // 2)
    if n % 2 != 0:
        result = "4" + result
    print(result)
