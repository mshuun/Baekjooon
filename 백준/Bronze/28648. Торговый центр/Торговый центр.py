n = int(input())
min_time = float('inf')

for _ in range(n):
    t_i, l_i = map(int, input().strip().split())
    arrival_time = t_i + l_i
    if arrival_time < min_time:
        min_time = arrival_time

print(min_time)
