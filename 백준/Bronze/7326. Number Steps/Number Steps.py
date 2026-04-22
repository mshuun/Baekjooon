n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    if x == y:
        if x%2 == 1:
            print(x*2-1)
        else:
            print(x*2)
    elif x == y+2:
        if x%2 == 1:
            print(x*2-3)
        else:
            print(x*2-2)
    else:
        print("No Number")
