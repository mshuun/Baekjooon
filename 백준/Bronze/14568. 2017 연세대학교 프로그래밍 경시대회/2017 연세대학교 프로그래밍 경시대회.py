n = int(input())
r = 0
for a in range(2,n+1,2):
    for b in range(1,n-a):
        c=n-a-b 
        if c>=b+2:
            r+=1
print(r)
