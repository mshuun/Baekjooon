n = int(input())
for i in range(n):
    o, p = map(int, input().split())

    def aaa(a, b):
        while b != 0:
            r = a % b
            a = b
            b = r
        return a
    k = aaa(o, p)
    print(int(o*p/k))
