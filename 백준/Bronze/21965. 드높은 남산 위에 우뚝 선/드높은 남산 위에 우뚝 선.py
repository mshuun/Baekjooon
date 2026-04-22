n = int(input())
a = list(map(int,input().split()))
dec = 0
fal = 0
for i in range(1,n):
    if a[i-1] > a[i] and dec == 0:
        dec = 1
    if dec == 1 and a[i-1] <= a[i]:
        fal = 1
    if dec == 0 and a[i-1] >= a[i]:
        fal = 1
if fal == 1:
    print("NO")
else:
    print("YES")