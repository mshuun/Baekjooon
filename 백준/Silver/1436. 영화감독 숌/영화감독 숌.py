n = int(input())
count = 0
number = 0
last = 0
while count != n:
    number += 1
    num = list(str(number))
    six = 0
    for i in range(len(num)):
        if num[i] == '6':
            six += 1
        else:
            six = 0
        if six == 3:
            break
    if six == 3:
        count += 1
        last = number
print(number)
