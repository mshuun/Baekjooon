import sys
print = sys.stdout.write
input = sys.stdin.readline

n = int(input())
names = set()
for _ in range(n):
    name,a = input().split()
    if a == 'enter':
        names.add(name)
    else:
        names.discard(name)
names = list(names)
names.sort(reverse=True)
for i in names:
    print(i)
    print('\n')