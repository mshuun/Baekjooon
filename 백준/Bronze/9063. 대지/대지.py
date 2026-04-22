m = []
for i in range(int(input())):
    a, b = map(int, input().split())
    m.append([a, b])
left_bot = [min([i[0] for i in m]), min([i[1] for i in m])]
right_top = [max([i[0] for i in m]), max([i[1] for i in m])]
print((right_top[0]-left_bot[0])*(right_top[1]-left_bot[1]))