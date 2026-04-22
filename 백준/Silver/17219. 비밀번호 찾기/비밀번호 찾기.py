n, m = map(int, input().split())
pw = dict()
for i in range(n):
    site, password = input().split()
    pw[site] = password
for i in range(m):
    print(pw[input()])