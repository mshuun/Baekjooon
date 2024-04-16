import sys
input = sys.stdin.readline
A = input().rstrip().split()
B = input().rstrip()
A = [i[:len(B)] for i in A if i != B]
print(A.count(B))
