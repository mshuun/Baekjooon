#include <stdio.h>

#define MAX_SIZE 100

int main() {
    int K, N, M, c = 0, A[MAX_SIZE], B[MAX_SIZE];
    
    scanf("%d %d", &K, &N);
    for (int i = 0; i < N; ++i) scanf("%d", &A[i]);
    
    scanf("%d", &M);
    for (int i = 0; i < M; ++i) scanf("%d", &B[i]);
    
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < M; ++j)
            if (A[i] + K == B[j]) ++c;
    
    printf("%d\n", c);
    
    return 0;
}
