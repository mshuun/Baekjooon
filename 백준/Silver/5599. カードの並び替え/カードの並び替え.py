n = int(input())
cards = list(range(1, 2*n + 1))
for _ in range(int(input())):
    op = int(input())
    if op == 0:
        a = cards[:n]
        b = cards[n:]
        cards = [val for pair in zip(a, b) for val in pair]
    else:
        cards = cards[op:] + cards[:op]
print(*cards,sep='\n')