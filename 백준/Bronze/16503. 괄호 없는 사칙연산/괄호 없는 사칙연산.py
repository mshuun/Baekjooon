a, x, b, y, c = list(input().split())
a, b, c = int(a), int(b), int(c)


def P(a, b):
    if a < 0:
        return -((-a)//b)
    elif b < 0:
        return -(a//(-b))
    else:
        return a//b


if x == '+':
    if y == '+':
        A = (a + b) + c
        B = a + (b + c)
    elif y == '-':
        A = (a + b) - c
        B = a + (b - c)
    elif y == '*':
        A = (a + b) * c
        B = a + (b * c)
    else:
        A = P((a + b), c)
        B = a + P(b, c)
elif x == '-':
    if y == '+':
        A = (a - b) + c
        B = a - (b + c)
    elif y == '-':
        A = (a - b) - c
        B = a - (b - c)
    elif y == '*':
        A = (a - b) * c
        B = a - (b * c)
    else:
        A = P((a - b), c)
        B = a - P(b, c)
elif x == '*':
    if y == '+':
        A = (a * b) + c
        B = a * (b + c)
    elif y == '-':
        A = (a * b) - c
        B = a * (b - c)
    elif y == '*':
        A = (a * b) * c
        B = a * (b * c)
    else:
        A = P((a * b), c)
        B = a * P(b, c)
else:
    if y == '+':
        A = P(a, b) + c
        B = P(a, (b + c))
    elif y == '-':
        A = P(a, b) - c
        B = P(a, (b - c))
    elif y == '*':
        A = P(a, b) * c
        B = P(a, (b * c))
    else:
        A = P(P(a, b), c)
        B = P(a, P(b, c))
if A > B:
    A, B = B, A
print(A)
print(B)
