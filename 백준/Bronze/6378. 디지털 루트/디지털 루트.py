while True:
    n = input()
    if n == '0':
        break
    
    while len(n) > 1:
        digit_sum = 0
        for digit in n:
            digit_sum += int(digit)
        n = str(digit_sum)
    
    print(n)
