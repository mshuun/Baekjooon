point = 0
for i in range(6):
    if input() == 'W':
        point += 1
if point == 1 or point == 2:
    print(3)
elif point == 3 or point == 4:
    print(2)
elif point == 5 or point == 6:
    print(1)
else:
    print(-1)