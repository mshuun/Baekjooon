#include <stdio.h>

int main() {
    int n, d;
    scanf("%d %d", &n, &d);

    int a[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += a[i];
    }

    for (int i = 0; i < n; i++) {
        printf("%d\n", a[i] * d / sum);
    }

    return 0;
}
