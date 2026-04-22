W, N = input().split()
N = int(N)

r = []

for i in range(N):
    arr = list(map(int, input().split()))
    narr = []
    for n in arr:
        if n == 2:
            narr.append(5)
        elif n == 5:
            narr.append(2)
        elif n == 1 or n == 8:
            narr.append(n)
        else:
            narr.append("?")
    r.append(narr)

if W == "L" or W == "R":
    for row in r:
        print(*(row[::-1]))
else:
    for row in r[::-1]:
        print(*row)
