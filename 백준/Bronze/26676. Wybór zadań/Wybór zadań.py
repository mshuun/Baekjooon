def c(p):
    A = {f"{B}{C}": 0 for B in range(1, 6) for C in 'ABC'}
    for E in p:
        if E in A: A[E] += 1
    for B in range(1, 5):
        for C in 'ABC':
            if A[f"{B}{C}"] < 1: return "NIE"
    return "NIE" if any(A[f"5{C}"] < 2 for C in 'ABC') else "TAK"
input()
print(c(input().split()))
