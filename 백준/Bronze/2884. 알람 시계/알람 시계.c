#include <stdio.h>
int main(){
    int h;
    int m;
    scanf("%d %d",&h,&m);
    int time = (h*60 + m - 45) % 1440;
    if(time<0){
        time = time + 1440;
    }
    h = time/60;
    m = time%60;
    printf("%d %d",h,m);
    return 0;
}