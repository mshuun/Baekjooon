l=[]
r=[]
for i in range(97,123):
    l.append(chr(i))
inp = list(input())
for a in range(len(l)):
    for b in range(len(inp)):
        if l[a] == inp[b] :
            r.append(b)
            break
        elif b == len(inp)-1 :
            r.append(-1)
for j in range(len(l)):
    print(r[j],end=' ')