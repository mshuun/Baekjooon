x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

distance_bessie = max(abs(x3 - x1), abs(y3 - y1))
distance_daisy = abs(x3 - x2) + abs(y3 - y2)

if distance_bessie < distance_daisy:
    print('bessie')
    
elif distance_bessie == distance_daisy:
    print('tie')
    
else:
    print('daisy')
