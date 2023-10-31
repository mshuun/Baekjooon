import sys
input = sys.stdin.readline

def prime_list(n):
    sosu = [1] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sosu[i] == 1:
            for j in range(i+i, n, i):
                sosu[j] = 0
    return [[i for i in range(2, n) if sosu[i]],sosu]
a = prime_list(1000000)
b = a[1]
a = a[0]
while 1:
    n = int(input())
    if n == 0: break
    for i in a:
        if b[n-i]:
            print(f'{n} = {i} + {n-i}')
            break