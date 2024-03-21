n = int(input())
a = list(map(int, input().split()))
cards = []
group = []
last = a[0]-1
for card in a:
    if card - last == 1:
        group.append(card)
        last = card
    else:
        cards.append(group)
        group = [card]
        last = card
if len(group) > 0:
    cards.append(group)
r = 0
for i in cards:
    r += i[0]
print(r)
