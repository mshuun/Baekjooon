def ccw(ax, ay, bx, by, cx, cy):
    return (ax*by + bx*cy + cx*ay) - (bx*ay + cx*by + ax*cy)


def is_intersecting(x1, x2, x3, x4):
    return min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2)


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

ccw123 = ccw(x1, y1, x2, y2, x3, y3)
ccw124 = ccw(x1, y1, x2, y2, x4, y4)
ccw341 = ccw(x3, y3, x4, y4, x1, y1)
ccw342 = ccw(x3, y3, x4, y4, x2, y2)

if ccw123 * ccw124 == 0 and ccw341 * ccw342 == 0:
    print(1 if is_intersecting(x1, x2, x3, x4) else 0)
elif ccw123 * ccw124 <= 0 and ccw341 * ccw342 <= 0:
    print(1)
else:
    print(0)
