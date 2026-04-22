n = int(input())
skill = input()
sk = 0
lr = 0
cnt = 0
for com in skill:
    if com == "S":
        sk += 1
    elif com == "L":
        lr += 1
    elif com == "K":
        if sk == 0:
            break
        else:
            sk -= 1
            cnt += 1
    elif com == "R":
        if lr == 0:
            break
        else:
            lr -= 1
            cnt += 1
    else:
        cnt += 1
print(cnt)