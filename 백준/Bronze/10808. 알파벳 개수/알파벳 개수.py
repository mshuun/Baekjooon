a = list(input())
alphabet = list('abcdefghijklmnopqrstuvwxyz')
result = []
for i in alphabet:
    result.append(a.count(i))
print(*result)