t = 1
while True:
    n = [int(input())]
    if n == [0]: break
    n.append(n[0] * 3)
    if n[0] % 2 == 0:
        n.append(n[1] // 2)
    else:
        n.append((n[1] + 1)//2)
    n.append(n[2] * 3)
    n.append(n[3] // 9)
    if n[1] % 2 == 0: oe = 'even'
    else: oe = 'odd'
    print(f'{t}. {oe} {n[4]}')
    t += 1