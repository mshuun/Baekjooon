import sys
input = sys.stdin.readline
print = sys.stdout.write

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    calls = [tuple(map(int, input().split()))[2:] for _ in range(N)]
    for _ in range(M):
        start, duration = map(int, input().split())
        end = start + duration
        count = sum(1 for call_start, call_duration in calls if not (end <= call_start or start >= call_start + call_duration))
        print(str(count))
        print('\n')
