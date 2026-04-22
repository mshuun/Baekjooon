N, A, B, C, D = map(int, input().split())
if N % A == 0:
    X = N//A
else:
    X = N//A + 1
if N % C == 0:
    Y = N//C
else:
    Y = N//C + 1
print(min(X*B, Y*D))