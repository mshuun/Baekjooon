#include <stdio.h>
int main() {
    int a;
    scanf("%d", &a);
    printf("%f\n", 100.0/a);
    printf("%f\n", 100.0/(100.0-a));
    return 0;
}
