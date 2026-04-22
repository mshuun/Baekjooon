a = int(input())
aa = a
cnt = 0
while True :
    a = ((a%10)*10)+((a//10+a%10)%10)
    cnt += 1
    if aa == a :
        print(cnt)
        break