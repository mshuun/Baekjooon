N,B,C = map(int,input().split())
An = list(map(int, input().split())) + [0, 0]  
cost = 0
if B<C:
    cost = sum(An)*B
else:
    def f(d, m, s):
        global cost
        for i in d:
            An[i] -= m
        cost += s * m

    for i in range(N):
        if An[i+1] > An[i+2]:
            f([i, i+1], min(An[i], An[i+1] - An[i+2]), B+C)
            f([i, i+1, i+2], min(An[i:i+3]), B+2*C)
            f([i], An[i], B)
        else:
            f([i, i+1, i+2], min(An[i:i+3]), B+2*C)
            f([i, i+1], min(An[i], An[i+1]), B+C)
            f([i], An[i], B)
        An[i] = 0

print(cost)
