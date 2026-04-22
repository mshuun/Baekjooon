n,k = map(int,input().split())
dead = list()
live = list()
for i in range(n):
    live.append(i+1)
target = k-1
for i in range(n):
    dead.append(live[target])
    del live[target]
    if len(live) == 0 :
        break
    target += k-1
    if target >= len(live):
        target = target % len(live)

print('<',end='')
for i in range(len(dead)):
    if i == len(dead)-1:
        print(dead[i],end='>')
    else :print(dead[i],end=', ')