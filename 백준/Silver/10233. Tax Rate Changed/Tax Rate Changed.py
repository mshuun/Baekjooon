import sys
input = sys.stdin.readline

while True:
    x, y, s = map(int,input().split())
    if x == 0 and y == 0 and s == 0:
        break
    max_after_tax_price = 0
    for before_tax_price1 in range(1, s):
        for before_tax_price2 in range(1, s):
            if before_tax_price1 + before_tax_price2 + (before_tax_price1 * x // 100) + (before_tax_price2 * x // 100) == s:
                after_tax_price1 = before_tax_price1 + (before_tax_price1 * y // 100)
                after_tax_price2 = before_tax_price2 + (before_tax_price2 * y // 100)
                max_after_tax_price = max(max_after_tax_price, after_tax_price1 + after_tax_price2)
    print(max_after_tax_price)