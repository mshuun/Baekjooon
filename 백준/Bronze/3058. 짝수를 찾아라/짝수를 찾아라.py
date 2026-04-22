for _ in range(int(input())):
    a = list(map(int, input().split()))
    a = [i for i in a if i % 2 == 0]
    print(sum(a), min(a))