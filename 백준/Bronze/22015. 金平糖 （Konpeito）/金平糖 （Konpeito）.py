a = list(map(int, input().split()))
print(sum([max(a)-i for i in a]))