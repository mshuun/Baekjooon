#include <stdio.h>

int main() {
    int c = 0;
    while (1) {
        int n;
        scanf("%d", &n);
        if (n == -1)
            break;
        c += n;
    }
    printf("%d\n", c);
    return 0;
}
