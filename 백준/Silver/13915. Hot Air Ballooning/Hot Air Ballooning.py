while 1:
    try:
        print(len(set([frozenset(input()) for _ in range(int(input()))])))
    except EOFError:
        break