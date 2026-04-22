a = input()
cnt = 0
for i in range(int(len(a)/2)):
    if a[i] == a[len(a)-i-1]:
        cnt += 1
if cnt == int(len(a)/2):
    print('1')
else:
    print('0')
