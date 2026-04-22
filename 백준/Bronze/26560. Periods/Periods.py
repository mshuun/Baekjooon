n = int(input())
for _ in range(n):
    s = input()
    if not s.endswith('.'):
        s += '.'
    print(s)
