n = input()

count = 0
for digit in n:
    if digit == '0':
        count += 1

for digit in n[::-1]:
    if digit == '0':
        count -= 1
    else:
        break

print(count)
