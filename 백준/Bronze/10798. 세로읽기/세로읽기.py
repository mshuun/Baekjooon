brd = []
for i in range(5):
    brd.append(list(input()))
for a in range(15):
    for b in range(5):
        if len(brd[b])>=a+1 :
            print(brd[b][a],end='')