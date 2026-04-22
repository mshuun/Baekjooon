#include <stdio.h>

int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    c -= 3;
    while (c <= 0) c += a;
    b += c;
    if (b > a) b %= a;
    if (b == 0) b = a;

    printf("%d\n", b);
    return 0;
}
