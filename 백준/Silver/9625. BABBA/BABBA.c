#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int a = 1, b = 0;
    for (int i = 0; i < n; i++) {
        int temp = a;
        a = b;
        b = temp + b;
    }

    printf("%d %d\n", a, b);
    return 0;
}
