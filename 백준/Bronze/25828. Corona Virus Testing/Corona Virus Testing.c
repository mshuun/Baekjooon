#include <stdio.h>

int main() {
    int g,p,t;
    scanf("%d %d %d",&g,&p,&t);
    int way1 = g*p;
    int way2 = g+p*t;
    if(way1>way2){
        printf("2");
    }
    else if(way1<way2){
        printf("1");
    }
    else{
        printf("0");
    }
    return 0;
}
