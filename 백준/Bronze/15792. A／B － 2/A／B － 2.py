from decimal import Decimal, getcontext
getcontext().prec = 1001
A, B = map(Decimal, input().split())
print(A / B)
