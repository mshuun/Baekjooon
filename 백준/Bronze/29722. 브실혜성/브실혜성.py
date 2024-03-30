y, m, d = map(int, input().split('-'))
N = int(input())

days = y*360 + (m-1)*30 + (d-1) + N

y = days // 360
days %= 360
m = days // 30 + 1
d = days % 30 + 1

print(f'{y}-{m:02d}-{d:02d}')
