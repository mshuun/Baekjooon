import hashlib
a = input()
print(hashlib.md5(a.encode('utf-8')).hexdigest())