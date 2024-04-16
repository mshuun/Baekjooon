A,B=input().split(),input()
print([s[:len(B)]for s in A if s!=B].count(B))