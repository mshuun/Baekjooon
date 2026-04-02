import sys
print(*sorted([int(i[::-1]) for i in sys.stdin.read().split()[1:]]),sep="\n")