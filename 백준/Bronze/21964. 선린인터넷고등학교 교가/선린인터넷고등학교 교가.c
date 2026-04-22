#include <stdio.h>
#include <string.h>

int main() {
    int n;
    char a[100000]; 
    scanf("%d", &n);
    scanf("%s", a);
    printf("%s\n", a + strlen(a) - 5);
    return 0;
}
