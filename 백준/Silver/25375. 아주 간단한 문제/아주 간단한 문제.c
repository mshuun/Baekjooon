#include <stdio.h>

int main()
{
    int t;
    scanf("%d",&t);
    long long int a,b;
    for(int i;i<t;i++)
    {
        scanf("%lld %lld",&a,&b);
        if(b%a == 0 && a<b){
            printf("1\n");
        }
        else{
            printf("0\n");
        }
    }
    return 0;
}
