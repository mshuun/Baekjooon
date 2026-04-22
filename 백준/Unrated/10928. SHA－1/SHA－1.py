import hashlib
a = input()
print(hashlib.sha1(a.encode('utf-8')).hexdigest())