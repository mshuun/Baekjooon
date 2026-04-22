#include <stdio.h>

int main() {
    int c, a, b;
    scanf("%d", &c);
    scanf("%d %d", &a, &b);
    
    int m = a / 2 + b;
    int r = (m < c) ? m : c;
    
    printf("%d\n", r);
    
    return 0;
}
