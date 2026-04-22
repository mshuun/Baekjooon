import math

X, Y = map(int, input().split())
Z = math.trunc(100 * Y / X)

W = 1000000000

def search():
    start = 0
    end = W
    while start <= end:
        mid = (start + end) // 2
        if math.trunc(((Y + mid) / (X + mid)) * 100) > Z:
            end = mid - 1
        else:
            start = mid + 1
    print(end + 1)

if Z >= 99:
    print(-1)
else:
    search()