def a():
    b,c=map(int,input().split(':'))
    return b*60+c
A = [a() for _ in ' '*4]
z = 1
for i in range(1440):
    if A[0] == A[1]:
        z = 0
        print(['Satur','Sun','Mon','Tues','Wednes','Thurs','Fri'][(A[0]%10080)//1440] + 'day')
        print(f'{(A[0]%1440)//60:02}:{A[0]%60:02}')
        break
    elif A[0] > A[1]:
        A[1] += A[3]
    else:
        A[0] += A[2]
if z:
    print('Never')

