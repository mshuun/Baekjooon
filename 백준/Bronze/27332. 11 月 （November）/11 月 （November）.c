#include <stdio.h>
int main(){
    int a,b;
    scanf("%d",&a);
    scanf("%d",&b);
    int c = a + b*7;
    if(c>30){
        printf("0");
    }else{
        printf("1");}
    return 0;
}
