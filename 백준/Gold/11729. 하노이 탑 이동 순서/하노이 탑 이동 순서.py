n = int(input())
result = []
def hanoi(n,ox,tx,mx):
    if n == 1:
        result.append([ox,tx])
    else:
        hanoi(n-1,ox,mx,tx)
        result.append([ox,tx])
        hanoi(n-1,mx,tx,ox)
hanoi(n,1,3,2)
print(len(result))
for i in result:
    print(*i)