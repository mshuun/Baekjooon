A = input()
for b in list(input().split()):
    A = A.replace(b, b.lower())
print(A)
