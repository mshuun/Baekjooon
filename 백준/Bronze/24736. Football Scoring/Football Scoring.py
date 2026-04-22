a = [6, 3, 2, 1, 2]
b = list(map(int, input().split()))
c = list(map(int, input().split()))
print(sum([b[i]*a[i] for i in range(5)]), sum([c[i]*a[i] for i in range(5)]))