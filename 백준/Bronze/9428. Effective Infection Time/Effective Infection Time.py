n = int(input())

for _ in range(n):
    im, iy= map(int, input().split())
    sm, sy = map(int, input().split())

    if iy == sy:
        print("{:.4f}".format(0.5 * (sm - im) / (13 - im)))
    else:
        print("{:.4f}".format(0.5 + (sy - iy - 1) + (sm - 1) / 12.0))