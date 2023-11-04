def ccw(ax, ay, bx, by, cx, cy):
    return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

ccw123 = ccw(x1, y1, x2, y2, x3, y3)
ccw124 = ccw(x1, y1, x2, y2, x4, y4)
ccw341 = ccw(x3, y3, x4, y4, x1, y1)
ccw342 = ccw(x3, y3, x4, y4, x2, y2)

if ccw123 * ccw124 == 0 and ccw341 * ccw342 == 0:
    if (min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4)) and (min(y1, y2) <= max(y3, y4) and max(y1, y2) >= min(y3, y4)):
        print(1)
    else:
        print(0)
else:
    print(1 if ccw123 * ccw124 <= 0 and ccw341 * ccw342 <= 0 else 0)
