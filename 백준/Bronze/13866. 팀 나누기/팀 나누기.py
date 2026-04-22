a = list(map(int, input().split()))
a.sort()
print(max(a[0]+a[3], a[1]+a[2])-min(a[0]+a[3], a[1]+a[2]))