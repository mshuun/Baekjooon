import bisect

N,K,T = map(int,input().split())
shark = sorted([*map(int,input().split())])
for i in range(K):
    d = bisect.bisect_left(shark,T)-1
    if d<0:
        break
    T += shark[d]
    shark.pop(d)
print(T)