n = int(input())
print('int a;')
print('int *ptr = &a;')
if n > 1:
    print('int **ptr2 = &ptr;')
    for i in range(2, n):
        print('int {}ptr{} = &ptr{};'.format('*'*(i+1), i+1, i))