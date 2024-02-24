n,k = map(int, input().split())
print('YES' if sum(i//2+i%2 for i in list(map(int, input().split())))>=n else 'NO')