n = int(input())
owon = n//5
yeewon = (n-owon*5)//2

while owon*5 + yeewon*2 != n:
    owon -= 1
    yeewon = (n-owon*5)//2
    if owon == -1:
        break

if  owon == -1:
    print(-1)
else:
    print(owon+yeewon)