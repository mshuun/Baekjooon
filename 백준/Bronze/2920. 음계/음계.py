a = list(map(int,input().split()))
k=0
if a[0] == 1:
    k=1
    for i in range(8):
        if a[i] != i+1 :
            k=0
elif a[0] == 8:
    k=2
    for i in range(8):
        if a[i] != 8-i :
            k=0
else : k=0
if k == 0 :print('mixed')
elif k ==1 :print('ascending')
else :print('descending')