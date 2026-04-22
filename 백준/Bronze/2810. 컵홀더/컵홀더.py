n=int(input())
cnt=0
seat=list(input())
for i in range(n):
    if i>0 and seat[i-1] == 'L' and seat[i] == 'L':
        seat[i-1] = 'S'
        seat[i] = 'X'
for i in range(n):
    if seat[i] == 'S':
        cnt += 1
cupHolder = cnt + 1
if cupHolder>n :
    print(n)
else :
    print(cupHolder)