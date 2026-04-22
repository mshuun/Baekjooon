N = int(input())

start_year = 2024
start_month = 8

add = (N - 1) * 7
total_month = start_month + add

year = start_year + (total_month - 1) // 12
month = (total_month - 1) % 12 + 1

print(year, month)
