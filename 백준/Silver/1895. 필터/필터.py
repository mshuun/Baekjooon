R, C = map(int, input().split())
image = [[*map(int,input().split())] for _ in range(R)]
T = int(input())

rr = 0
for i in range(R - 2):
    for j in range(C - 2):
        new = []
        for a in range(3):
            for b in range(3):
                new.append(image[i + a][j + b])
    
        new.sort()
        if new[4] >= T:
            rr += 1
            
print(rr)