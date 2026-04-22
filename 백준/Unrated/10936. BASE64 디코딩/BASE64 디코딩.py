import base64
a = input()
a = base64.b64decode(a)
print(a.decode('utf-8'))