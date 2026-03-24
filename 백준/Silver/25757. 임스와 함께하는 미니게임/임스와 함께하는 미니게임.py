N,g = input().split()
a = len({input() for _ in range(int(N))})
if g == "Y":
    print(a)
elif g == "F":
    print(a//2)
else:
    print(a//3)