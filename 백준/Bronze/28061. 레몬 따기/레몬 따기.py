N = int(input())
tree = list(map(int, input().split()))
m = -1
for i in range(N):
    tree[i] -= N - i
print(max(tree))
