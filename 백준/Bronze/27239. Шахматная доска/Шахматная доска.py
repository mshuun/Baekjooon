n = int(input())
x = 'habcdefg'[n%8]
if n%8 == 0:
    y = n//8
else:
    y = n//8 + 1
print(x+str(y))