P = 1500000
M = 1000000
fibo = [0, 1]


def fib(n):
    if n < len(fibo):
        return fibo[n]

    else:
        for i in range(len(fibo), n + 1):
            fibo.append((fibo[i - 2]+fibo[i - 1]) % M)
        return fibo[-1]


N = int(input())

print(fib(N % P) % P)
