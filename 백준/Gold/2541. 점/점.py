def can_generate(a, b, points):
    def abs_diff(k):
        return abs(k)

    d = abs_diff(b - a)
    if a == b:
        a, b = 1, 1
    else:
        while d % 2 == 0:
            d //= 2
        if a < b:
            a, b = 1, 1 + d
        else:
            a, b = 1 + d, 1

    results = []
    for x, y in points:
        if (a <= b) != (x <= y):
            results.append("N")
        else:
            dd = abs_diff(y - x)
            if d * dd == 0:
                if d == dd:
                    results.append("Y")
                else:
                    results.append("N")
            else:
                if dd % d == 0:
                    results.append("Y")
                else:
                    results.append("N")
    return results


a, b = map(int, input().split())
points = []
while True:
    try:
        points.append(map(int, input().split()))
    except EOFError:
        break

results = can_generate(a, b, points)
for result in results:
    print(result)
