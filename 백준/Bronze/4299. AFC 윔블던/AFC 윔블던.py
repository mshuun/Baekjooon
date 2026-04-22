a, b = map(int, input().split())
find = True
for i in range(a+1):
    if find:
        for j in range(i, a+1):
            if a == i+j and b == max(i, j)-min(i, j):
                print(j, i)
                find = False
                break
if find == True:
    print(-1)