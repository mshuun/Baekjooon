N = int(input())
for _ in range(N):
    G = int(input())
    students = [int(input()) for _ in range(G)]
    n = 1
    while True:
        ns = set()
        for student in students:
            ns.add(student%n)
        if len(ns) == G:
            print(n)
            break
        n += 1