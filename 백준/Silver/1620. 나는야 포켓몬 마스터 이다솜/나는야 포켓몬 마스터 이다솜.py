import sys
input = sys.stdin.readline
n, m = map(int, input().split())
pokedex = {}
for i in range(1, n+1):
    name = input().rstrip()
    pokedex[i] = name
    pokedex[name] = i
for i in range(m):
    a = input().rstrip()
    if a.isdigit():
        a = int(a)
        print(pokedex[a])
    else:
        print(pokedex[a])
