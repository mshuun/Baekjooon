a = []
b = []
for i in range(4):
    a.append(int(input()))
for i in range(2):
    b.append(int(input()))
print(sum(a)-min(a)+max(b))
