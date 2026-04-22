#include <stdio.h>
int main(){
    int cost1,cost2,n;
    scanf("%d %d",&cost1,&cost2);
    scanf("%d",&n);
    for(int i=0;i<n;++i){
        int use;
        int price;
        scanf("%d",&use);
        if(use<=1000){
            price = cost1*use;
        }
        else{
            price = cost1*1000 + cost2*(use-1000);
        }
        printf("%d %d\n",use,price);
    }
    return 0;
}
