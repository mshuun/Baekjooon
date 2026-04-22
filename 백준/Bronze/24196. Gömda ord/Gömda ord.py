a = input()
b = ''
c = 0
while True:
    b += a[c]
    c += ord(a[c]) - 64
    if c >= len(a):
        break
print(b)