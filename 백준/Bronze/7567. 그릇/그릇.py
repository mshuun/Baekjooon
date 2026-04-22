a = list(input())
k = 3
h = 0
for i in range(len(a)):
    if a[i] == '(':
        s = 0
    else:
        s = 1
    if s == k:
        h += 5
    else:
        h += 10
    k = s
print(h)
