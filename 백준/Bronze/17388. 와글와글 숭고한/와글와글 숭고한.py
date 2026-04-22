a = list(map(int, input().split()))
if sum(a) >= 100:
    print('OK')
else:
    print(['Soongsil', 'Korea', 'Hanyang'][a.index(min(a))])