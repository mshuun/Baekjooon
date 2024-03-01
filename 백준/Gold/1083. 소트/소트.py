n = int(input())
e = list(map(int, input().split()))
S = int(input())
f = 1
for i in range(n):
    max_pos = i
    for j in range(i + 1, min(i + S + 1, n)):
        if e[j] > e[max_pos]:
            max_pos = j

    while max_pos > i:
        e[max_pos], e[max_pos - 1] = e[max_pos - 1], e[max_pos]
        max_pos -= 1
        S -= 1
        if S == 0:
            f = 0
            print(*e)
            break
if f:
    print(*e)