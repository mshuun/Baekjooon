n = int(input())
a = []
b = []
for i in range(n):
    a.append(int(input()))
for i in range(1,a[-1]+1):
    if i not in a:
        b.append(i)
if len(b) == 0:
    print("good job")
else:
    for i in b:
        print(i)