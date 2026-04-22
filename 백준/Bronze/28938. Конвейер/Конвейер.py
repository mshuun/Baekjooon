n = int(input())
f = sum(list(map(int, input().split())))

if f > 0:
    print("Right")
elif f < 0:
    print("Left")
else:
    print("Stay")
