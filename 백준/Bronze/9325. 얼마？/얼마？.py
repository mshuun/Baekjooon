for _ in range(int(input())):
    cost = int(input())
    for _ in range(int(input())):
        a, b = map(int, input().split())
        cost += a * b
    print(cost)