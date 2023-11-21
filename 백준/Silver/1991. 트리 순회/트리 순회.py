class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(node):
    if node:
        print(node.data, end="")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end="")
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end="")

nodes = {chr(i + 65): Node(chr(i + 65)) for i in range(26)}

n = int(input())
for _ in range(n):
    root, left, right = input().split()
    if left != ".":
        nodes[root].left = nodes[left]
    if right != ".":
        nodes[root].right = nodes[right]

preorder(nodes['A'])
print()
inorder(nodes['A'])
print()
postorder(nodes['A'])
