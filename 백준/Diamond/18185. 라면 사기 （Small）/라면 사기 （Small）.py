N = int(input()) 
An = list(map(int, input().split())) + [0, 0]  
cost = 0

for i in range(N):
    if An[i+1] > An[i+2]:
        m = min(An[i], An[i+1] - An[i+2])
        An[i] -= m
        An[i+1] -= m
        cost += 5 * m

        m = min(An[i:i+3])
        An[i] -= m
        An[i+1] -= m
        An[i+2] -= m
        cost += 7 * m

        cost += 3 * An[i]
        An[i] = 0
    else:
        m = min(An[i:i+3])
        An[i] -= m
        An[i+1] -= m
        An[i+2] -= m
        cost += 7 * m

        m = min(An[i], An[i+1])
        An[i] -= m
        An[i+1] -= m
        cost += 5 * m

        cost += 3 * An[i]
        An[i] = 0
print(cost)