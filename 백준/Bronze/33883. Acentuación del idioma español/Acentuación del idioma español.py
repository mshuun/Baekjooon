s = input()
if s[-1] in 'aeiouns':
    r=2
else:
    r=1
for i in range(len(s)-1,-1,-1):
    if s[i] in 'aeiou':
        r -= 1
    if r == 0:
        print(i+1)
        break
if r != 0:
    print(-1)