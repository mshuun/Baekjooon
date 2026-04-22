import hashlib
a = input()
print(hashlib.sha512(a.encode('utf-8')).hexdigest())