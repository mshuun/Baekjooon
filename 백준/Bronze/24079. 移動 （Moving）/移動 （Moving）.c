#include<stdio.h>

int main() {
    int x, y, z;
    scanf("%d", &x);
    scanf("%d", &y);
    scanf("%d", &z);

    if (x + y <= z) {
        printf("1\n");
    } else {
        printf("0\n");
    }

    return 0;
}
