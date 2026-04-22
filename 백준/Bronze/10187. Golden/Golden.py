# BOJ 10187
# Golden
n = int(input())
golden = (1 + 5 ** 0.5) / 2
for i in range(n):
    a,b = map(float,input().split())
    if a < b:
        a,b = b,a
    ratio = a / b
    if golden*0.99 <= ratio <= golden* 1.01:
        print('golden')
    else:
        print('not')