a = input()
b = []
for i in range(0,len(a)):
    b.append(a[i:])
b.sort()
print(*b,sep='\n')