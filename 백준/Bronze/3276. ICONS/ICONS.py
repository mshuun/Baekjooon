import math

N = int(input())

rows = math.ceil(math.sqrt(N))
columns = math.ceil(N / rows)

print(rows, columns)
