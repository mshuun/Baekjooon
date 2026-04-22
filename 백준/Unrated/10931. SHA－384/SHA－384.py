import hashlib
a = input()
print(hashlib.sha384(a.encode('utf-8')).hexdigest())