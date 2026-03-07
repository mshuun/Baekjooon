import sys
input = sys.stdin.read
choco = [*map(int,input().split())]

n = choco[0]
h = choco[1:n+1]
w = choco[n+1:]

hw = sorted(zip(h, w))

total_w = sum(w)
max_choco = 0

for height, width in hw:
    now = height * total_w
    if now > max_choco:
        max_choco = now
    total_w -= width

print(max_choco)