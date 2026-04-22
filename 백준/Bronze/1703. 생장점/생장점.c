#include <stdio.h>

int main() {
    while (1) {
        int n, a, b, c, s = 1;
        scanf("%d", &n);
        if (!n) return 0;
        
        while (n--) {
            scanf("%d %d", &a, &b);
            s = s * a - b;
        }
        printf("%d\n", s);
    }
}
