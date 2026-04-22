N = int(input())
maxW = 0
rope = list()
for i in range(N):
    rope.append(int(input()))
rope.sort(reverse=True)

maxW = max([rope[i] * (i + 1) for i in range(N)])
print(maxW)
