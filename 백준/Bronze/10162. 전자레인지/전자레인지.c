#include <stdio.h>

int main()
{
    int T;
    scanf("%d", &T);

    int A = T / 300;
    T %= 300;
    int B = T / 60;
    T %= 60;
    int C = T / 10;
    T %= 10;

    if (T == 0)
        printf("%d %d %d\n", A, B, C);
    else
        printf("-1\n");

    return 0;
}
