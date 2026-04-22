for _ in range(int(input())):
    n = bin(int(input()))[2:]
    n = n[::-1]
    print(*[i for i in range(len(n)) if n[i] == '1'])