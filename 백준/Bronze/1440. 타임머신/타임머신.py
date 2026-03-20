a,b,c = map(int,input().split(":"))
print(sum([1 for h,m,s in[[a,b,c],[a,c,b],[b,a,c],[c,a,b],[b,c,a],[c,b,a]]if 0<h<13 and 0<=m<60 and 0<=s<60]))