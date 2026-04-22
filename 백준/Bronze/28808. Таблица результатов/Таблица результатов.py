n, m = map(int, input().split())
solved = 0

for _ in range(n):
    results = input()
    if '+' in results:
        solved += 1

print(solved)
