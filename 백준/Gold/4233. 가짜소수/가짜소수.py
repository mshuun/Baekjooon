def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def fermat(p, a):
    if is_prime(p):
        return "no"
    return "yes" if pow(a, p, p) == a else "no"


while 1:
    p, a = map(int, input().split())
    if p == 0 and a == 0:
        break
    print(fermat(p, a))
