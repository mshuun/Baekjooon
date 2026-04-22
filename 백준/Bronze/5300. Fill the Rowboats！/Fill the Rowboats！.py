n = int(input())
count = 0
a = []
for i in range(1, n+1):
    a.append(i)
    count += 1
    if count == 6:
        a.append('Go!')
        count = 0
if count != 0:
    a.append('Go!')
print(*a)
