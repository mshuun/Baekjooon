n = int(input())
a = list(input().split())
r = 1
for i in range(n):
    if a[i] != "mumble":
        a[i] = int(a[i])
        if i+1 != a[i]:
            r = 0
    else:
        a[i] = i+1
if r:
    print("makes sense")
else:
    print("something is fishy")