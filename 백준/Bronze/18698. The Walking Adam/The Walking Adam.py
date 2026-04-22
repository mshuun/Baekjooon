T = int(input())
for _ in range(T):
    case = input()
    u = 0
    for i in range(len(case)):
        if case[i] == 'U':
            u += 1
        else:
            break
    print(u)