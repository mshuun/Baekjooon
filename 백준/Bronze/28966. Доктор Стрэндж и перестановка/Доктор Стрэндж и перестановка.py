n = int(input())
a = list(map(int, input().split()))
wrong = 0
wrongs = []
for i in range(1,n+1):
    if i%2 != a[i-1]%2:
        wrong += 1
        wrongs.append(i)
if wrong == 2:
    if a[wrongs[0]-1]%2 != a[wrongs[1]-1]%2:
        print(wrongs[0],wrongs[1])
    else:
        print(-1,-1)
elif wrong == 0 and n>2:
    print(1,3)
else:
    print(-1,-1)