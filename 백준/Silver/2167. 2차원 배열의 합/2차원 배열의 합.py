import sys
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
k = int(input())
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    h = 0
    for j in range(x1-1, x2):
        for l in range(y1-1, y2):
            h += array[j][l]
    print(str(h))
    print('\n')
