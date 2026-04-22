n = int(input())
k = int(input())
card = 60 + k
if n < card :
    print(n * 1500)
else :
    print(card * 1500 + (n - card) * 3000)