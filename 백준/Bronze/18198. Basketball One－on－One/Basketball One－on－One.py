game = input()
a=0
b=0
for i in range(len(game)//2):
    if game[2*i] == 'A':
        a += int(game[2*i+1])
    else:
        b += int(game[2*i+1])
if a>b:
    print('A')
elif a<b:
    print('B')