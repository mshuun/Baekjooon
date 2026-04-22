#include <stdio.h>

int main() {
    int a, b, c, d, e, f, g;
    scanf("%d %d", &a, &b);
    scanf("%d %d", &c, &d);
    scanf("%d %d %d", &e, &f, &g);
    long long int result = (long long int)(a * b + c * d) * e * f * g;
    printf("%lld", result);
    return 0;
}
