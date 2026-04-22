import sys
input = sys.stdin.readline
print = sys.stdout.write
for _ in range(int(input())):
    a = min(map(int, input().split()))
    print(str(a))
    print('\n')