n = int(input())
if n == 0:
    print('divide by zero')
else:
    records = list(map(int, input().split()))
    exp = sum(record*(1/n) for record in records)
    if n == 0:
        print('divide by zero')
    else:
        print("{:.2f}".format(sum(records)/n/exp))