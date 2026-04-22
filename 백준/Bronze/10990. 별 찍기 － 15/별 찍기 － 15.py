n = int(input())
print(' '*(n-1), end='*\n')
for i in range(2, n+1):
    print(' '*(n-i), end='*')
    print(' '*(2*i-3), end='*\n')