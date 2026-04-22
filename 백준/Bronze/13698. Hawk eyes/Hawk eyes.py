b = [0,1,0,0,2]
for c in list(input()):
    x,y={'A':[1,2],'B':[1,3],'C':[1,4],'D':[2,3],'E':[2,4],'F':[3,4]}[c]
    b[x],b[y]=b[y],b[x]
print(*[b.index(1),b.index(2)])