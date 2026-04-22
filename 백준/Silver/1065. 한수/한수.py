def arithmetic_sequences(maxnum):
    return min(maxnum, 99) + sum([i[2] == i[1] + (i[1] - i[0]) for i in (list(map(int, str(n))) for n in range(100, min(maxnum + 1, 1001)))])

inp = int(input())
print(arithmetic_sequences(inp))
