socks = []
for _ in range(5):
    sock = int(input())
    if sock not in socks:
        socks.append(sock)
    else:
        socks.remove(sock)
print(*socks)