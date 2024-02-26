for _ in range(int(input())):
    times = list(input().split())
    angles = []
    for time in times:
        H, M = map(int, time.split(':'))
        hour_angle = (H % 12) * 30 + M * 0.5
        minute_angle = M * 6 
        angle_diff = abs(hour_angle - minute_angle)
        angle = min(angle_diff, 360 - angle_diff)
        angles.append((angle, time))
    angles.sort()
    print(angles[2][1])
