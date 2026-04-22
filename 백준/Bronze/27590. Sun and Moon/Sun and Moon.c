#include <stdio.h>
int main(){
    int ds,ys,dm,ym;
    scanf("%d %d",&ds,&ys);
    scanf("%d %d",&dm,&ym);
    int ts = ys-ds;
    int tm = ym-dm;
    while(ts!=tm){
        if(ts>tm){
            tm += ym;
        } else{
            ts += ys;
        }
    }
    printf("%d",ts);
    return 0;
}
