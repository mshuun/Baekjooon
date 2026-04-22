temperature = int(input())
atmospheric_pressure = 5*temperature - 400
print(atmospheric_pressure)
if atmospheric_pressure > 100:
    print(-1)
elif atmospheric_pressure == 100:
    print(0)
else:
    print(1)