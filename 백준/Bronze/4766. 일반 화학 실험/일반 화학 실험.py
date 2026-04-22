prev_temp = None

while True:
    temp = float(input())
    
    if temp == 999:
        break
    
    if prev_temp is not None:
        temp_diff = round(temp - prev_temp, 2)
        print("{:.2f}".format(temp_diff))
    
    prev_temp = temp
