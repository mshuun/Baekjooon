A_start = list(map(int,input().split(':')))
B_start = list(map(int,input().split(':')))
A_cycle = list(map(int,input().split(':')))
B_cycle = list(map(int,input().split(':')))
A_start = A_start[0]*60 + A_start[1]
B_start = B_start[0]*60 + B_start[1]
A_cycle = A_cycle[0]*60 + A_cycle[1]
B_cycle = B_cycle[0]*60 + B_cycle[1]
c = 1
for i in range(1440):
    if A_start == B_start:
        c = 0
        h = (A_start%1440)//60
        m = A_start%60
        d = (A_start%10080)//1440
        print(['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'][d])
        print(f'{h:02}:{m:02}')
        break
    elif A_start > B_start:
        B_start += B_cycle
    else:
        A_start += A_cycle
if c:
    print('Never')