input()
w=map(int, input().split())
input()
ns={0}
for i in w:ns|={abs(j-i)for j in ns}|{j+i for j in ns}
print(*('Y'if t in ns else'N'for t in map(int,input().split())))