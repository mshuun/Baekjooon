n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

card_counts = {}

for card in cards:
    if card not in card_counts:
        card_counts[card] = 1
    else:
        card_counts[card] += 1

for target in targets:
    if target in card_counts:
        print(card_counts[target], end=' ')
    else:
        print(0, end=' ')
