T = int(input())
for i in range(T):
    number, valid = map(int, input().split())
    bin_number = bin(number)[2:]
    if valid == bin_number.count('1') % 2:
        print('Valid')
    else:
        print('Corrupt')
