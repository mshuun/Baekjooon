n = int(input())
s = 0
while n>9:
    n=eval('*'.join(list(str(n))))
    s+=1
print(s)