n = int(input())
numbers = list(map(int, input().split()))

e = 0
o = 0
for number in numbers:
    if number % 2 == 0:
        e += 1
    else:
        o += 1

if e > o:
    print("Happy")
else:
    print("Sad")
