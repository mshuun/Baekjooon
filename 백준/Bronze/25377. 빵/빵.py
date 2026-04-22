n = int(input())
time = []
for i in range(n):
    a, b = map(int, input().split())
    if a <= b:
        time.append(b)
if len(time) == 0:
    print(-1)
else:
    print(min(time))