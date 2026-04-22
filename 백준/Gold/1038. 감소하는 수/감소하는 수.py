from itertools import combinations as c
n = int(input())
r = []
for i in range(1, 11):
    for j in c(range(10), i): r.append(int("".join(map(str, sorted(list(j), reverse=1)))))
r.sort()
print(r[n] if 1023 > n else -1)