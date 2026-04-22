from math import comb as c
for i in range(int(input())):
    a, b = map(int, input().split())
    print(c(b, b-a))