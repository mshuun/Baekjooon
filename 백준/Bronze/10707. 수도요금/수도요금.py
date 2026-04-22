def X(P, A):
    return P*A


def Y(P, B, C, D):
    if P <= C:
        return B
    else:
        return B + (P-C)*D


a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())
x = X(p, a)
y = Y(p, b, c, d)
print(min(x, y))