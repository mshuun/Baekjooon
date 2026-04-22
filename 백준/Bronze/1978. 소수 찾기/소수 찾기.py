n = int(input())
numbers = map(int,input().split())
primes=0
for i in numbers:
    prime = True
    for j in range(2,int(i ** 1/2)+1):
        if i%j == 0 :
            prime=False
            break
    if i == 1 : prime = False
    if prime : primes += 1
print(primes)