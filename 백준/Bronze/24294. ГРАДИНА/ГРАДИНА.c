#include <stdio.h>

int main() {
    int a,b,c,d;
    scanf("%d%d%d%d",&a,&b,&c,&d);
    if(a>c){
        printf("%d",4+2*a+2*(b+d));
    }else{
        printf("%d",4+2*c+2*(b+d));
    }

    return 0;
}
