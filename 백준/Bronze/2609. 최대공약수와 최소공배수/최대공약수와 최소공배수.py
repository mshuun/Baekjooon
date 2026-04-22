o,p = map(int, input().split())
def aaa(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
k=aaa(o,p)
print(int(k))
print(int(o*p/k))
