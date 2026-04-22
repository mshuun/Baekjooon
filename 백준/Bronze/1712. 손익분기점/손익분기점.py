A,B,C = map(int,input().split())
make = 0
earn = 0
if B<C:
    make = (earn +A)//(C-B)+1
else :
    make = -1
print(make)