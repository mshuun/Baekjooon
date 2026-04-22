n = int(input())
for i in range(n):
    p, t = map(int, input().split())
    dead = t//7
    born = t//4
    print(p-dead+born)