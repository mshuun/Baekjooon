while (n := int(input())) != -1:
    total_distance = previous_time = 0
    for _ in range(n):
        s, t = map(int, input().split())
        total_distance += s * (t - previous_time)
        previous_time = t
    print(f"{total_distance} miles")
