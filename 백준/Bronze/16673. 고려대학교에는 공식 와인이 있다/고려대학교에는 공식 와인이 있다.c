#include <stdio.h>

int main() {
    int c,p,k;
    scanf("%d %d %d",&c,&k,&p);
    int sum = 0;
    for(int i=1;i<=c;i++){
        sum += k*i+p*i*i;
    }
    printf("%d",sum);
}
