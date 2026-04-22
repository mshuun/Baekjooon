#include <stdio.h>
int main()
{
    int a,b;
    scanf("%d",&a);
    scanf("%d",&b);
    int h =(a+b)%12;
    if (h==0)
    {
        h=12;
    }
    printf("%d\n",h);
    return 0;
}
