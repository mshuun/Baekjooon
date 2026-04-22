ca = list(input())
ca.append('None')
ca.append('None')
cnt = 0
i=0
while True:
    if ca[i] == 's' or ca[i] == 'z' :
        if ca[i+1] == '=' :
            cnt += 1
            i +=2
        else :
            cnt += 1
            i += 1
    elif ca[i] == 'c' :
        if ca[i+1] == '=' or ca[i+1] == '-' :
            cnt += 1
            i += 2
        else :
            cnt += 1
            i += 1
    elif ca[i] == 'l' or ca[i] == 'n' :
        if ca[i+1] == 'j' :
            cnt += 1
            i += 2
        else :
            cnt += 1
            i += 1
    elif ca[i] == 'd' :
        if ca[i+1] == '-' :
            cnt += 1
            i += 2
        elif ca[i+1] == 'z':
            if ca[i+2] == '=':
                cnt += 1
                i += 3
            else :
                cnt += 1
                i += 1
        else :
            cnt += 1
            i += 1
    else :
        cnt += 1
        i += 1
    if ca[i] == 'None' :
        break
print(cnt)