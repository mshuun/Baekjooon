r = 0
b = 0
n=int(input())
if n == 1:
    print(0)
else:
    box = []
    for _ in range(n):
        box.append(list(input()))
    w = 1
    for i in range(n):
        for j in range(len(box[i])):
            try:
                color = box[i][j]
                if  color == 'R':
                    if box[i+1][j] == 'R':
                        box[i+1][j] = 0
                    else:
                        w = 0
                    if box[i+1][j+1] == 'R':
                        box[i+1][j+1] = 0
                    else:
                        w = 0
                elif color == 'B':
                    if box[i][j+1] == 'B':
                        box[i][j+1] = 0
                    else:
                        w = 0
                    if box[i+1][j+1] == 'B':
                        box[i+1][j+1] = 0
                    else:
                        w = 0
            except:
                w = 0
    print(w)
