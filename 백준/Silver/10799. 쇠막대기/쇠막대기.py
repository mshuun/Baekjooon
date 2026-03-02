s = input().replace("()", "*")
total = 0
op = 0

for i in s:
    if i == "(":
        op += 1
    elif i == "*":
        total += op
    else:
        op -= 1
        total += 1

print(total)