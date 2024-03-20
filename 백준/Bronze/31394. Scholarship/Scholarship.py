n = int(input())
satis = 0
per = 1
s = 0
for i in range(n):
    a = int(input())
    s += a
    if a == 3:
        satis = 1
    if a != 5:
        per = 0
avg = s / n
if satis:
    print('None')
elif per:
    print('Named')
elif avg>=4.5:
    print('High')
else:
    print('Common')