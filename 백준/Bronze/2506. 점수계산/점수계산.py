n = int(input())
a = list(map(int, input().split()))
score = 0
point = 1
for i in range(n):
    if a[i] == 1:
        score += point
        point += 1
    else:
        point = 1
print(score)