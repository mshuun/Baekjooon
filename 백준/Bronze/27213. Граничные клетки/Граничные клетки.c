#include <stdio.h>

int main() {
    int m, n;
    scanf("%d %d", &m, &n);

    int a = (2 * m) + (2 * n) - 4;

    if (m == 1 || n == 1)
        a = (m + n) - 1;

    printf("%d\n", a);

    return 0;
}
