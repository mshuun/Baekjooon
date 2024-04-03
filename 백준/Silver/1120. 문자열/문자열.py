A, B = input().split()

r = 99
x = len(A)
y = len(B)
for i in range(y-x+1):
    c = 0
    b = B[i:i+x]
    for i in range(x):
        if A[i] != b[i]:
            c += 1
    r = min(r, c)

print(r)
