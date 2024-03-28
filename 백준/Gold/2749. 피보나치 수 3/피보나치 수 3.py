a = 0
b = 1
for i in range(int(input()) % 1500000-1):
    a, b = b, (a+b) % 1000000
print(b % 1500000)
