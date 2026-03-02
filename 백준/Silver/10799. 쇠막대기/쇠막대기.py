s = input()
t = 0
total = 0
op = 0
for i in s:
    if i == "(":
        op += 1
        t = 1
    elif t == 1:
        t = 0
        op -= 1
        total += op
    else:
        t = 0
        op -= 1
        total += 1
print(total)