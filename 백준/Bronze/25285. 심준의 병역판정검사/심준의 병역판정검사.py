T = int(input())
for i in range(T):
    height, weight = map(int, input().split())
    BMI = weight / (height/100)**2
    if height < 140.1:
        print(6)
    elif height < 146:
        print(5)
    elif height < 159:
        print(4)
    elif height < 161:
        if 16 <= BMI < 35:
            print(3)
        else:
            print(4)
    elif height < 204:
        if BMI < 16 or BMI >= 35:
            print(4)
        elif 16 <= BMI < 18.5 or 30 <= BMI < 35:
            print(3)
        elif 18.5 <= BMI < 20 or 25 <= BMI < 30:
            print(2)
        else:
            print(1)
    else:
        print(4)
