angles = set()

for m in range(720):
    hour_pos = (m // 12) * 6
    min_pos = (m % 60) * 6
    
    diff = abs(hour_pos - min_pos)
    angle = min(diff, 360 - diff)
    angles.add(angle)

while True:
    try:
        line = input()
        if not line:
            break
        a = int(line)
        if a in angles:
            print("Y")
        else:
            print("N")
    except EOFError:
        break