#include <stdio.h>
int main() {
    int a;
    scanf("%d", &a);
    for(int i = 1; i <= a; i++) {
        if(i%7 == 0 && i%11 == 0){
            printf("Wiwat!\n");
        }
        else if(i%7==0){
            printf("Hurra!\n");
        }
        else if(i%11==0){
            printf("Super!\n");
        }
        else{
            printf("%d\n", i);
        }
    }
    return 0;
}
