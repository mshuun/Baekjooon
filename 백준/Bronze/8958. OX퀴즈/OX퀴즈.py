n = int(input())
for i in range(n) :
    score = 0
    cnt = 0
    a = list(input())
    for j in range(len(a)) :
        if a[j] == 'O' :
            if cnt != 0 :
                cnt += 1
                score += cnt
            else :
                cnt += 1
                score += 1
        else :
            cnt = 0
    print(score)