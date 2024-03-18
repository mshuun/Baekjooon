#include <stdio.h>

int main() {
    int N, X, K;
    scanf("%d %d %d", &N, &X, &K);

    for (int i = 0; i < K; i++) {
        int a, b;
        scanf("%d %d", &a, &b);

        if (a == X) {
            X = b;
        } else if (b == X) {
            X = a;
        }
    }

    printf("%d\n", X);

    return 0;
}
