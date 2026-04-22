l = int(input())
a=input()
h=0
for i in range(l):
    h += (ord(a[i])-96) * 31 ** i
print(h%1234567891)