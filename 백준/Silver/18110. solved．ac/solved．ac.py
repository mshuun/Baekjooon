from sys import stdin
input = stdin.readline


def rounds(num):
    return int(num) + [0, 1][num - int(num) >= 0.5]


a = []
n = int(input())
if n != 0:
    for _ in range(n):
        a.append(int(input()))
    cut = rounds(len(a)*0.15)
    a.sort()
    if cut != 0:
        a = a[cut:-cut]
    if len(a) != 0:
        print(rounds(sum(a)/len(a)))
    else:
        print(0)
else:
    print(0)
