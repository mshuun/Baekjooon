scores = list(map(int, input().split()))
if sum(scores) < 100:
    print('none')
else:
    for i in range(len(scores)):
        if scores[i] > (i//2+1)*100:
            print('hacker')
            break
    else:
        print('draw')