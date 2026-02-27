#include <unistd.h>
#define S 1024
char b[S]; int p,n,o;

int gc(){ return p<n?b[p++]:((n=syscall(0,0,b,S))>0?(p=1,b[0]):0); }
int ri(){
    int c=gc(),s=1,x=0;
    while(c<=32) c=gc();
    if(c==45) s=-1,c=gc();
    while((unsigned)(c-48)<10) x=x*10+(c&15),c=gc();
    return x*s;
}
void oc(char c){ if(o>=S) syscall(1,1,b,o),o=0; b[o++]=c; }
void wi(int x){
    if(!x){ oc(48); return; }
    if(x<0) oc(45),x=-x;
    char t[12]; int i=0;
    while(x) t[i++]=x%10+48,x/=10;
    while(i) oc(t[--i]);
}

typedef signed char i8;

void __libc_start_main(){
    i8 A[100][100],B[100][100];
    int N=ri(),M=ri(),K;
    for(int i=0;i<N;i++) for(int j=0;j<M;j++) A[i][j]=ri();
    ri(); K=ri();
    for(int i=0;i<M;i++) for(int j=0;j<K;j++) B[i][j]=ri();

    for(int i=0;i<N;i++) for(int j=0;j<K;j++){
        int s=0; for(int k=0;k<M;k++) s+=A[i][k]*B[k][j];
        wi(s); oc(j+1==K?10:32);
    }
    syscall(1,1,b,o);
    _exit(0);
}
main;