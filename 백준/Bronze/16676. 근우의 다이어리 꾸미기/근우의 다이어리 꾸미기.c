#include <stdio.h>

int main() {
    int n;
    int c = 1;
    int a = 11;
    
    scanf("%d", &n);

    while (a <= n) {
        c++;
        a = a * 10 + 1;
    }

    printf("%d", c);
    return 0;
}
