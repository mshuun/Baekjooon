#include <stdio.h>

int main() {
    int n, a, b, A = 0, B = 0;

    scanf("%d", &n);
    while (n--) {
        scanf("%d %d", &a, &b);
        if (a > b)
            A++;
        else if (a < b)
            B++;
    }
    
    printf("%d %d", A, B);
    return 0; 
}
