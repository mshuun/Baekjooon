for _ in range(int(input())):
    n, g = input().split()
    g = int(g)

    if 97 <= g <= 100:
        grade = "A+"
    elif 90 <= g <= 96:
        grade = "A"
    elif 87 <= g <= 89:
        grade = "B+"
    elif 80 <= g <= 86:
        grade = "B"
    elif 77 <= g <= 79:
        grade = "C+"
    elif 70 <= g <= 76:
        grade = "C"
    elif 67 <= g <= 69:
        grade = "D+"
    elif 60 <= g <= 66:
        grade = "D"
    else:
        grade = "F"

    print(f"{n} {grade}")
