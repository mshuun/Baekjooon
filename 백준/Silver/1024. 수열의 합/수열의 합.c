main(N,L,i,a,j)
{
scanf("%d%d",&N,&L);
for (i=L;i <= 100;i++)
{
a=(N-i*(i-1)/2)/i;
if (a >= 0 && N == a*i + i*(i-1)/2)
{
for (j=0;j<i;j++)printf("%d ",a+j);
return 0;
}
}
printf("-1");
return 0;
}
