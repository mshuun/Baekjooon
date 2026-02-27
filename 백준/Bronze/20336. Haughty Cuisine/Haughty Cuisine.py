n = int(input())
best = None
for _ in range(n):
    parts = input().split()
    d = int(parts[0])
    dishes = parts[1:1+d]
    if best is None:
        best = dishes

print(len(best))
for x in best:
    print(x)