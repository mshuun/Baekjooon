n = int(input())
for i in range(n+1):
    if i**2 == n:
        print(f'The largest square has side length {i}.')
        break
    if i**2 > n:
        print(f'The largest square has side length {i-1}.')
        break