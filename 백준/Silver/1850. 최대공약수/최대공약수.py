o, p = map(int, input().split())

def aaa(a, b):
    while b:
        a, b = b, a % b
    return a

print(aaa(o, p) * '1')