import sys
from decimal import Decimal
input = sys.stdin.readline
T = int(input())
for i in range(T):
    n, m = map(Decimal, input().split())
    print(f'Scenario #{i+1}:')
    print(int((m-n+1)*(m+n)/2))
    print()
