N = int(input())
A = [1, 2]
for i in range(3, N):
    A.append(i)
A.append(997)
print(N)
print(*A)
