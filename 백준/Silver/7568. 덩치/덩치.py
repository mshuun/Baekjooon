n = int(input())
l = list()
scores = []
for i in range(n):
    a, b = map(int, input().split())
    l.append([a, b])
for i in l:
    score = 0
    for j in l:
        if i[0] < j[0]:
            if i[1] < j[1]:
                score += 1
    scores.append(score+1)
print(*scores)
