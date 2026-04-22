n = int(input())
max_area = 0

for _ in range(n):
    h_i, w_i = map(int, input().strip().split())
    area = h_i * w_i
    if area > max_area:
        max_area = area

print(max_area)
