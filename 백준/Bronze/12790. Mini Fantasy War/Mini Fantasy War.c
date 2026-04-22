#include <stdio.h>
int main(){
    int n,hp,mp,atk,def,hp1,mp1,atk1,def1;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        scanf("%d %d %d %d %d %d %d %d", &hp, &mp, &atk, &def, &hp1, &mp1, &atk1, &def1);
        hp += hp1;
        mp += mp1;
        atk += atk1;
        def += def1;
        if(hp < 1) hp = 1;
        if(mp < 1) mp = 1;
        if(atk < 0) atk = 0;
        printf("%d\n", hp + 5*mp + 2*atk + 2*def);
    }
}