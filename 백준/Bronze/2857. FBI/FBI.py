result = []
for i in range(5):
    a = input()
    for j in range(len(a)-2):
        if a[j:j+3] == 'FBI':
            result.append(i+1)
            break
if result:
    print(*result)
else:
    print('HE GOT AWAY!')