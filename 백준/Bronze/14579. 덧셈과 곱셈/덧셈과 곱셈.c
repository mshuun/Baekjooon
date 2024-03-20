#include <stdio.h>

int sum(int n) {
    int total = 0;
    for (int i = 1; i <= n; i++) {
        total += i;
    }
    return total;
}

int main() {
    int a, b, result = 1;
    scanf("%d %d", &a, &b);
    
    for (int i = a; i <= b; i++) {
        result = (result * sum(i)) % 14579;
    }
    
    printf("%d\n", result);
    return 0;
}
