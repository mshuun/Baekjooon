a, b, c = map(int, input().split())
s = (b**2 + c ** 2) ** 0.5
for i in range(a):
    if int(input()) <= s:
        print("DA")
    else:
        print("NE")