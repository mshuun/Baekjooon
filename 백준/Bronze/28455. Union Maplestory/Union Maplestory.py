n = int(input())
levels = []

for i in range(n):
    levels.append(int(input()))

levels.sort(reverse=True)
top_levels = levels[:42]

alv = sum(top_levels)
c = []

for lv in top_levels:
    if lv >= 250:
        c.append(5)
    elif lv >= 200:
        c.append(4)
    elif lv >= 140:
        c.append(3)
    elif lv >= 100:
        c.append(2)
    elif lv >= 60:
        c.append(1)
    else:
        c.append(0)

print(alv, sum(c))