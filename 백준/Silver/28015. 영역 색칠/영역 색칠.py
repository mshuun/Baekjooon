sero, garo = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(sero)]
cnt = 0
new_paper = []
for line in paper:
    new_line = []
    last_color = -1
    for can in line:
        if can != last_color:
            last_color = can
            new_line.append(can)
    new_paper.append(new_line)
new_new_paper = []
for line in new_paper:
    new_line = []
    for can in line:
        if can != 0:
            new_line.append(can)
        elif len(new_line) != 0:
            new_new_paper.append(new_line)
            new_line = []
    if len(new_line) != 0:
        new_new_paper.append(new_line)
        new_line = []
for line in new_new_paper:
    cnt += line.count(0)+1 + min(line.count(2), line.count(1))
    if len(line) != 1:
        if line[0] == 0:
            cnt -= 1
        if line[-1] == 0:
            cnt -= 1
print(cnt)
