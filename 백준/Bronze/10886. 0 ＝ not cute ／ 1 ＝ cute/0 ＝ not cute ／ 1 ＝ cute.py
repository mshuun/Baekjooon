a = int(input())
y, n = 0, 0
for i in range(a):
    k = int(input())
    if k == 0:
        n += 1
    else:
        y += 1
if n>y :
    print("Junhee is not cute!")
else :
    print("Junhee is cute!")