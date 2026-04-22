import hashlib
a = input()
print(hashlib.sha224(a.encode('utf-8')).hexdigest())