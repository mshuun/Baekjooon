#include <unistd.h>
#include <sys/syscall.h>

#define RSZ (1<<18)  
#define WSZ (1<<15)  

#define readInt(n) {                          \
    while (*p <= 32) ++p;                     \
    int sgn = 1;                              \
    if (*p == '-') sgn = -1, ++p;             \
    n = 0;                                    \
    while ((unsigned)(*p - '0') < 10)         \
        n = n*10 + (*p++ & 15);               \
    n *= sgn;                                 \
}

static inline void flush(char *w, int *wi){
    if(*wi) syscall(SYS_write, 1, w, *wi), *wi = 0;
}

static inline void writeIntBuf(char *w, int *wi, int x){
    if (*wi > WSZ - 16) flush(w, wi);

    if (x == 0){ w[(*wi)++]='0'; return; }
    if (x < 0){ w[(*wi)++]='-'; x = -x; }

    char t[12];
    int n=0;
    while(x){ t[n++] = (char)('0' + (x%10)); x/=10; }
    while(n--) w[(*wi)++] = t[n];
}

__attribute__((noreturn))
int __libc_start_main() {
    static char r[RSZ];
    static char w[WSZ];
    int wi = 0;

    syscall(SYS_read, 0, r, RSZ);
    char *p = r;

    int N,M,K,M2;
    static int A[100][100];
    static int B[100][100];

    readInt(N); readInt(M);
    for(int i=0;i<N;i++)
        for(int k=0;k<M;k++)
            readInt(A[i][k]);

    readInt(M2); readInt(K); (void)M2;
    for(int k=0;k<M;k++)
        for(int j=0;j<K;j++)
            readInt(B[k][j]);
 
    for(int i=0;i<N;i++){
        for(int j=0;j<K;j++){
            int s=0;
            for(int k=0;k<M;k++) s += A[i][k]*B[k][j];
            writeIntBuf(w, &wi, s);
            w[wi++] = (j+1==K)?'\n':' ';
            if (wi > WSZ - 32) flush(w, &wi);
        }
    }

    flush(w, &wi);
    _exit(0);
}
int main;