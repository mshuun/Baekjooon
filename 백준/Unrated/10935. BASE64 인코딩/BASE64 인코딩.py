import base64
a = input()
a = a.encode('utf-8')
a = base64.b64encode(a)
a = a.decode('utf-8')
print(a)