snack = []
for i in range(3):
    price, weight = map(int, input().split())
    if price >= 500:
        price -= 50
    snack.append(weight/price)
print('SNU'[snack.index(max(snack))])
