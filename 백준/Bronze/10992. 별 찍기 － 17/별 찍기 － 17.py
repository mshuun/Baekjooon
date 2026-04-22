n = int(input())
print(' '*(n-1), end='*\n')
for i in range(2, n):
    print(' '*(n-i), end='*')
    print(' '*(2*i-3), end='*\n')
if n != 1:
    print('*'*(2*n-1))