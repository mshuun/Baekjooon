t = []
for i in range(3):
    a, b, c, d = map(int, input().split())
    start = a * 60 + b
    end = c * 60 + d
    if end < start:
        end += 1440 - start
        start = 0
    t.append(end-start)
print(f'{min(t) // 60}:{min(t) % 60:02d}')
print(f'{max(t) // 60}:{max(t) % 60:02d}')
