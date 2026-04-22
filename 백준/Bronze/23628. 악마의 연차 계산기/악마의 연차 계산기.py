y,m,d = map(int,input().split())
yy,mm,dd = map(int,input().split())
ad = (yy-y)*360 + (mm-m)*30 + dd - d

mmm = min(36,ad//30)
yyy = 0
for i in range(1,ad//360 + 1):
    yyy += 15 + (i-1)//2
print(yyy,mmm)
print(f"{ad}days")