while True:
    n = input()
    if n == '#':
        break
    n = list(n)
    a = list('aeiouAEIOU')
    s = 0
    for i in a:
        s += n.count(i)
    print(s)