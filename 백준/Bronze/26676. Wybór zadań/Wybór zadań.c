#include <stdio.h>
int main() {
    int n, c[15] = {0}, i;
    char p[3];
    for(scanf("%d", &n); n--; c[(p[0] - '1') * 3 + p[1] - 'A']++) scanf("%s", p);
    for(i = 0; i < 15; i++)
        if(c[i] < 1 + (i / 3 == 4))
            return !printf("NIE\n");
    printf("TAK\n");
}
