import sys
input = sys.stdin.readline

n = int(input())

l = []

for i in range(n):
    num = int(input())
    if num == 0:
        l.pop()
    else:
        l.append(num)

print(sum(l))
