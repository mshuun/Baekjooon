x, k = map(int, input().split())
max_snow = 1000*x
top = 7000*k
mid = 3500*k
bot = 1750*k
if max_snow >= top:
    print(top)
elif max_snow >= mid:
    print(mid)
elif max_snow >= bot:
    print(bot)
else:
    print(0)
