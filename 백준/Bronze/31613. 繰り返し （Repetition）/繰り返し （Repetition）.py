X,N=int(input()),int(input())
c=0
while X<N:c+=1;X=(X+1 if X%3==0 else X*2 if X%3==1 else X*3)
print(c)