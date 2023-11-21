def preorder(tree, node):
    if node != '.':
        print(node, end="")
        preorder(tree, tree[node][0])
        preorder(tree, tree[node][1])

def inorder(tree, node):
    if node != '.':
        inorder(tree, tree[node][0])
        print(node, end="")
        inorder(tree, tree[node][1])

def postorder(tree, node):
    if node != '.':
        postorder(tree, tree[node][0])
        postorder(tree, tree[node][1])
        print(node, end="")

n = int(input())
tree = {}
for _ in range(n):
    root, left, right = input().split()
    tree[root] = (left, right)

preorder(tree, 'A')
print()
inorder(tree, 'A')
print()
postorder(tree, 'A')
