for _ in range(int(input())):
    X,Y,x,y=map(int,input().split())
    if x>X or y>Y :
        print(X*Y)
    else:
        choco = [[1 for _ in range(X)] for _ in range(Y)]
        coco = X*Y
        for i in range(X):
            for j in range(Y):
                if choco[j][i]:
                    try:
                        choco[j+y][i+x] = 0
                        coco-=1
                    except:pass
        print(coco)