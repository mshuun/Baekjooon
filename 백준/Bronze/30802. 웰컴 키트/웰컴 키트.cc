#include<cstdio>
int n,a[6],t,p,s,i;int main(){scanf("%d",&n);while(i<6)scanf("%d",a+i++);scanf("%d%d",&t,&p);while(i--)s+=(a[i]+t-1)/t;printf("%d\n%d %d",s,n/p,n%p);}