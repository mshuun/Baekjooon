t = 0
for _ in range(9):
    if input().strip() == "Tiger":
        t += 1
print("Tiger" if t >= 5 else "Lion")