s = int(input())
a = int(input())
b = int(input())
price = 250
height = a
while height < s:
    price += 100
    height += b
print(price)