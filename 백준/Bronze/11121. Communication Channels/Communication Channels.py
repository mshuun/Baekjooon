t = int(input())


def is_ok(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return "ERROR"
    return "OK"


for _ in range(t):
    a, b = input().split()
    print(is_ok(a, b))