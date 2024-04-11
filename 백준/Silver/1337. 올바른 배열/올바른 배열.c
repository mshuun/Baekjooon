#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}

int main()
{
    int N, i, j, k, r = 5;
    int l[50];

    scanf("%d", &N);
    for (i = 0; i < N; i++)
    {
        scanf("%d", &l[i]);
    }
    qsort(l, N, sizeof(int), compare);
    for (i = 0; i < N; i++)
    {
        for (j = i; j < i + 5 && j < N; j++)
        {
            int z = j - i + 1;
            int sum = 0;
            for (k = i; k < j; k++)
            {
                sum += l[k + 1] - l[k];
            }
            if (sum < 5)
            {
                if (5 - z < r)
                {
                    r = 5 - z;
                }
            }
        }
    }

    printf("%d\n", r);

    return 0;
}
