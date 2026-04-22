from collections import Counter
N = int(input())
num = [int(input()) for _ in range(N)]
print(round(sum(num)/N))
num.sort()
print(num[N//2])
most = Counter(num)
most = most.most_common(2)
if len(most) == 2:
    if most[0][1] == most[1][1]:
        print(most[1][0])
    else:
        print(most[0][0])
else:
    print(most[0][0])
print(max(num)-min(num))
