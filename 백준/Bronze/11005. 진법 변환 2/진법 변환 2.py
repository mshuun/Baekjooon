n, b = map(int, input().split())
result = []

while n:
    r = n % b
    n //= b
    if r >= 10:
        result.append(chr(ord('A') + r - 10))
    else:
        result.append(str(r))

result.reverse()
print(''.join(result))