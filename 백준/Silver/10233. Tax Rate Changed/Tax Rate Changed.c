#include <stdio.h>
int A[1000][100];
int main(){
    for (int i=0;i<1000;i++)for (int t=0;t<100;t++)A[i][t]=i*(100+t)/100;
    while(1){
        int x,y,s;
        if(scanf("%d%d%d",&x,&y,&s)!=3)break;
        if(x==0)break;
        int B=s-1,C=0;
        for(int D=1;D<s;D++){if(B<D)break;int E=A[D][x],F=A[B][x];while(F+E>s){B-=1;if(B<D)break;F=A[B][x];}if(B>=D&&E+F==s)if(A[D][y]+A[B][y]>C)C=A[D][y]+A[B][y];}
        printf("%d\n",C);
    }
    return 0;
}
