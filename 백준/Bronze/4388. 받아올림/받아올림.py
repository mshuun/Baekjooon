def f(num1, num2):
    str_num1, str_num2 = str(num1), str(num2)
    carries, carry = 0, 0
    if len(str_num1) > len(str_num2):
        str_num2 = str_num2.zfill(len(str_num1))
    else:
        str_num1 = str_num1.zfill(len(str_num2))

    for i in range(len(str_num1) - 1, -1, -1):
        sum = int(str_num1[i]) + int(str_num2[i]) + carry
        if sum >= 10:
            carries += 1
            carry = 1
        else:
            carry = 0

    return carries

while True:
    num1, num2 = map(int, input().split())
    if num1 == 0 and num2 == 0:
        break
    print(f(num1, num2))
