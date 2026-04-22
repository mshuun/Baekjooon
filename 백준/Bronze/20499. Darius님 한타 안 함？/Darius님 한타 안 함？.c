#include <stdio.h>

int main() {
    int a, b, c;
    scanf("%d/%d/%d", &a, &b, &c);
    
    if (a + c < b || b == 0)
        printf("hasu\n");
    else
        printf("gosu\n");
    
    return 0;
}
