fibo = [0, 1]

for i in range(1, 90):
    fibo.append(fibo[i]+fibo[i-1])
print(fibo[int(input())])
