stamp = int(input())
price = int(input())
print(max(0, int(min([price, price-500, price*0.9, price-2000, price*0.75][0:stamp//5+1]))))
