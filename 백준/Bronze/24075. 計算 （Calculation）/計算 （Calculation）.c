#include <stdio.h>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    int a = n + m;
    int b = n - m;

    if (a >= b) {
        printf("%d\n%d\n", a, b);
    } else {
        printf("%d\n%d\n", b, a);
    }

    return 0;
}
