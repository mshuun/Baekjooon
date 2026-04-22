T = int(input())
result = [0,1,2,4]
for i in range(1,10):
    result.append(result[i]+result[i+1]+result[i+2])
for i in range(T):
    N = int(input())
    print(result[N])