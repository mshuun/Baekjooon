a, b, c = map(int, input().split())
i, j, k = map(int, input().split())
cocktail = min(a/i, b/j, c/k)
print(a-i*cocktail, b-j*cocktail, c-k*cocktail)
