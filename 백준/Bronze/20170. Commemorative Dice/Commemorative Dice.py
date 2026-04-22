import math

a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = sum(1 for i in a for j in b if i > j)

total_cases = 36
gcd_val = math.gcd(c, total_cases)

print(f"{c // gcd_val}/{total_cases // gcd_val}")