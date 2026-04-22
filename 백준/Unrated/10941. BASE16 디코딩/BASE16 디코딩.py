import base64
a = input()
a = base64.b16decode(a, casefold=False)
print(a.decode('utf-8'))