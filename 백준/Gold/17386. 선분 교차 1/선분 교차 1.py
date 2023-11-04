x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
ccw123 = (x1*y2+x2*y3+x3*y1) - (x2*y1+x3*y2+x1*y3)
ccw124 = (x1*y2+x2*y4+x4*y1) - (x2*y1+x4*y2+x1*y4)
ccw341 = (x3*y4+x4*y1+x1*y3) - (x4*y3+x1*y4+x3*y1)
ccw342 = (x3*y4+x4*y2+x2*y3) - (x4*y3+x2*y4+x3*y2)
r = 0
if ccw123*ccw124 == 0 and ccw341*ccw342 == 0:
    if x1 > x2:
        x2, x1 = x1, x2
    if x3 > x4:
        x3, x4 = x4, x3
    if x3 <= x4 and x1 <= x4:
        print(1)
    else:
        print(0)
elif ccw123*ccw124 <= 0 and ccw341*ccw342 <= 0:
    print(1)
else:
    print(0)
