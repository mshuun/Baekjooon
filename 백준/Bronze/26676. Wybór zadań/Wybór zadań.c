#include <stdio.h>
int main() {
    int n, c[15] = {0}, i, r, d;
    scanf("%d", &n);
    char p[3];
    while (n--) {
        scanf("%s", p);
        r = (p[0] - '1') * 3;
        d = p[1] - 'A';
        c[r + d]++;
    }
    for (i = 0; i < 15; i++)
        if (c[i] < 1 + (i / 3 == 4))
            return !printf("NIE\n");
    printf("TAK\n");
}
