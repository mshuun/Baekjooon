#include <stdio.h>
#include <math.h>

int main() {
    int T;
    scanf("%d", &T);

    for (int i = 0; i < T; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        a %= 10;

        if (a == 0) {
            printf("10\n");
        } else if (a == 1 || a == 5 || a == 6) {
            printf("%d\n", a);
        } else if (a == 4 || a == 9) {
            b %= 2;
            if (b == 0) {
                printf("%d\n", (int)pow(a, 2) % 10);
            } else {
                printf("%d\n", a);
            }
        } else if (a == 2 || a == 3 || a == 7 || a == 8) {
            b %= 4;
            if (b == 0) {
                printf("%d\n", (int)pow(a, 4) % 10);
            } else {
                printf("%d\n", (int)pow(a, b) % 10);
            }
        }
    }

    return 0;
}
