#include <stdio.h>

int main()
{
    int t, n;
    scanf("%d", &t);

    while (t--)
    {
        scanf("%d", &n);
        int player1Wins = 0, player2Wins = 0;

        for (int i = 0; i < n; i++)
        {
            char player1, player2;
            scanf(" %c %c", &player1, &player2);

            if (player1 == player2)
                continue;
            if ((player1 == 'R' && player2 == 'S') || (player1 == 'S' && player2 == 'P') || (player1 == 'P' && player2 == 'R'))
                player1Wins++;
            else
                player2Wins++;
        }

        if (player1Wins > player2Wins)
            printf("Player 1\n");
        else if (player1Wins < player2Wins)
            printf("Player 2\n");
        else
            printf("TIE\n");
    }

    return 0;
}
