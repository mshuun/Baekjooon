n = int(input())
a=2
cnt = 1
while True :
    if a<=n :
        a += 6*cnt
        cnt += 1
    else : break
print(cnt)