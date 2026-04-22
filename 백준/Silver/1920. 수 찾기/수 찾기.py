n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))


def binary_search(a, x):
    left = -1
    right = len(a)
    while right > left + 1:
        middle = (left + right) // 2
        if a[middle] < x:
            left = middle
        else:
            right = middle
    if right < len(a) and a[right] == x:
        return True
    else:
        return False


a.sort()
for i in b:
    if binary_search(a, i):
        print(1)
    else:
        print(0)
