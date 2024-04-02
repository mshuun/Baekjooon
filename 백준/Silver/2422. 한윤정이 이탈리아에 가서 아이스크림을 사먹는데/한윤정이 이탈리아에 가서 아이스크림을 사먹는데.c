#include <stdio.h>
#include <stdbool.h>

int main()
{
    int N, M;
    scanf("%d %d", &N, &M);
    bool bad[201][201] = {false};

    for (int i = 0; i < M; i++)
    {
        int a, b;
        scanf("%d %d", &a, &b);
        bad[a][b] = true;
        bad[b][a] = true;
    }

    int result = 0;
    for (int i = 1; i <= N; i++)
    {
        for (int j = i + 1; j <= N; j++)
        {
            if (bad[i][j])
                continue;
            for (int k = j + 1; k <= N; k++)
            {
                if (!bad[i][k] && !bad[j][k])
                {
                    result += 1;
                }
            }
        }
    }

    printf("%d\n", result);
    return 0;
}
