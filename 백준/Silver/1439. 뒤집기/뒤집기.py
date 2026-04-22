n = list(input())
a = [int(n[0])]
for i in range(1, len(n)):
    if n[i] == '0' and n[i-1] == '1':
        a.append(0)
    elif n[i] == '1' and n[i-1] == '0':
        a.append(1)
print(min(a.count(0), a.count(1)))