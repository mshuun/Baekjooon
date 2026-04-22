#include <stdio.h>
int main() {
    long long int N, M;
    scanf("%lld %lld", &N, &M);

    if (N % (M + 1) == 1) {
        printf("Can't win");
    } else {
        printf("Can win");
    }

    return 0;
}