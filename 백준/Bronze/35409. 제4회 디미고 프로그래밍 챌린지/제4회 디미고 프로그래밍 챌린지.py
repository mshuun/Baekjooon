import sys

h, m = map(int, sys.stdin.readline().split())

time = h * 60 + m

times = [
    (6*60 + 30, 9*60 + 0),
    (9*60 + 50, 10*60 + 0),
    (10*60 + 50, 11*60 + 0),
    (11*60 + 50, 12*60 + 0),
    (12*60 + 50, 13*60 + 50),
    (14*60 + 40, 14*60 + 50),
    (15*60 + 40, 15*60 + 50),
    (16*60 + 40, 22*60 + 50)
]

r = False
for start, end in times:
    if start <= time <= end:
        r = True
        break

if r:
    print("Yes")
else:
    print("No")