year_a, month_a, day_a = map(int, input().split())
year_b, month_b, day_b = map(int, input().split())
if (month_a < month_b) or (month_a == month_b and day_a <= day_b):
    print(year_b - year_a)
else:
    print(year_b - year_a - 1)
print(year_b - year_a+1)
print(year_b - year_a)