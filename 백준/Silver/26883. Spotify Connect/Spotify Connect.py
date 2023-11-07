n = int(input().strip())
logs = [input().strip().split() for _ in range(n)]

for i in range(n):
    logs[i][0] = int(logs[i][0])
    if logs[i][1] == 'mobile':
        logs[i][0] += 100
logs.sort()
now = False
time = 0
play = 0
for log in logs:
    if log[2] == 'play' and now == False:
        now = True
        play = log[0]
    elif log[2] == 'paus' and now == True:
        now = False
        time += log[0]-play
print(time)