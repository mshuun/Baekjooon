A, B, C = map(int, input().split())
if B in (1, 2):
    r = (A - 1) * 4 + 3
elif 3 <= B <= 5:
    r = A * 4 + 0
elif 6 <= B <= 8:
    r = A * 4 + 1
elif 9 <= B <= 11:
    r = A * 4 + 2
elif B == 12:
    r = A * 4 + 3
print(r - 8058)