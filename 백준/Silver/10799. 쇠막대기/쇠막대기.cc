#include<cstdio>
int main(){int c,p,o=0,t=0;while((c=getchar())>10){if(c<41)o++;else o--,t+=p<41?o:1;p=c;}printf("%d",t);}