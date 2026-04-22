n = int(input())
f = int(input())
while n%100 != 0 :
    n -= 1
while n%f != 0 :
    n += 1
n = str(n)
print(f'{n[-2]}{n[-1]}')
