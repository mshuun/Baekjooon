#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        int a;
        scanf("%d", &a);

        long long t = 0;
        for (int j = 1; j <= a; j++) {
            t += (long long)j * (j + 1) / 2;
        }

        printf("%lld\n", t);
    }

    return 0;
}
