n = int(input())
while n != 0:
    a = [int(input()) for _ in range(n)]
    a.reverse()
    for i in a:
        print(i)
    print(0)
    n = int(input())
