n, m = map(int, input().split())

def C(n, f):
    count = 0
    while n:
        n //= f
        count += n
    return count

A = C(n, 2) - C(m, 2) - C(n - m, 2)
B = C(n, 5) - C(m, 5) - C(n - m, 5)

print(min(A, B))
