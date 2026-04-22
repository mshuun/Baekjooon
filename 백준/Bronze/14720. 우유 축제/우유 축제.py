n = int(input())
m = list(map(int, input().split()))
a = 0
b = 0
for i in m:
    if i == a:
        b += 1
        a += 1
        if a == 3:
            a = 0
print(b)