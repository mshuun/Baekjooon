#include <stdio.h>
#include <string.h>

int main()
{
    int N;
    char K[100];

    scanf("%d", &N);

    for (int i = 0; i < N; i++)
    {
        scanf("%s", K);
        if ((K[strlen(K) - 1] - '0') % 2 == 0)
        {
            printf("even\n");
        }
        else
        {
            printf("odd\n");
        }
    }

    return 0;
}
