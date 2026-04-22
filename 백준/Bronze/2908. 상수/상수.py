a,b = input().split()
a = list(map(int,list(a)))
b = list(map(int,list(b)))
l=[a[2]*100 + a[1]*10 + a[0],b[2]*100 + b[1]*10 + b[0]]
print(max(l))