#include<stdio.h>
 
int main(){
    int q, a;
    scanf("%d", &q);
    for (int i = 0; i < q; i++){
        scanf("%d", &a);
        if ((a&(-a))==a)printf("1\n");
        else printf("0\n");
    }
}