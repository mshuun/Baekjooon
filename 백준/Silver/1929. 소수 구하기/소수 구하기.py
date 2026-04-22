a, n = map(int, input().split())
n = n+1
sieve = [True] * n
m = int(n ** 0.5)
for i in range(2, m + 1):
    if sieve[i]:
        for j in range(i+i, n, i):
            sieve[j] = False
primes = [i for i in range(2, n) if sieve[i]]
for i in range(len(primes)):
    if primes[i] >= a:
        print(primes[i])
