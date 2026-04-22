n = int(input())
for i in range(n-2, -1, -1):
    print('*' * (n-i-1) + ' ' * (2*i+2)+'*' * (n-i-1))
print('*' * (2*n))
for i in range(n-1):
    print('*' * (n-i-1) + ' ' * (2*i+2)+'*' * (n-i-1))
