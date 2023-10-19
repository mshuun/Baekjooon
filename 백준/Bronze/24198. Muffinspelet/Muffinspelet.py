# BOJ 24198
# Muffinspelet
n = int(input())
a = 0
b = 0
turn = 0
while n!=0:
    if(n%2 == 0):
        A = n//2
        B = n//2
    else:
        A = n//2 + 1
        B = n//2
    if turn == 0:
        b += max([A,B])
        n = min([A,B])
        turn = 1
    else:
        a += max([A,B])
        n = min([A,B])
        turn = 0
print(a,b)
