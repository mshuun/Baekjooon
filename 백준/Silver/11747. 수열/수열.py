N = int(input())
a = "".join([*input().split()])
while True:
    try:
        a = a+"".join([*input().split()])
    except EOFError:
        break
n = 0
while True:
    if str(n) not in a:
        print(n)
        break
    else:
        n += 1