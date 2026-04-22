#include <stdio.h>

int main() {
    int a, b, c, n = 0;
    scanf("%d %d", &a, &b);
    while (a--) {
        scanf("%d", &c);
        b -= c;
        if (b < 0) break;
        n++;
    }
    printf("%d", n);
    return 0;
}
