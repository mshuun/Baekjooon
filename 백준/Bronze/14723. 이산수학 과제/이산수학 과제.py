n = int(input())

line = 1
while n > line:
    n -= line
    line += 1

a = line - (n - 1)
b = n

print(a, b)