while True:
    B, N = map(int, input().split())
    if B == 0 and N == 0:
        break

    A = 1
    while A ** N < B:
        A += 1

    if abs((A - 1) ** N - B) < abs(A ** N - B):
        print(A - 1)
    else:
        print(A)
