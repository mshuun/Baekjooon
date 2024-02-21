answer = dict()
for i in range(1,10001):
    for j in range(100):
        if j+j*j>i:
            answer[i] = j-1
            break
T = int(input())
for i in range(T):
    d = int(input())
    print(answer[d])
   