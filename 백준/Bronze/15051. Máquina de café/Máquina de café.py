A1 = int(input())
A2 = int(input())
A3 = int(input())
time_1 = 2 * A2 + 4 * A3
time_2 = 2 * A1 + 2 * A3
time_3 = 4 * A1 + 2 * A2
min_time = min(time_1, time_2, time_3)
print(min_time)
