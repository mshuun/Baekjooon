C = []
for _ in range(int(input())):
    d, c = input().split()
    c = int(c)
    if d == 'jinju':
        D = c
    C.append(c)
print(D)
print(sum([1 for i in C if i > D]))
