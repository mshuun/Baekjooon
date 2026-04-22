#include <stdio.h>

int main() {
    int d[4] = {'N', 'E', 'S', 'W'};
    int sum = 0;
    
    for (int i = 0; i < 10; i++) {
        int a;
        scanf("%d", &a);
        sum += a;
    }
    
    printf("%c\n", d[sum % 4]);
    
    return 0;
}
