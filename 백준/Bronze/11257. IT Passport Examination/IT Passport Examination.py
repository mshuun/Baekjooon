for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    total = b + c + d
    result = 'PASS' if b >= 10.5 and c >= 7.5 and d >= 12 and total >= 55 else 'FAIL'
    print(a, total, result)
