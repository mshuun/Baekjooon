#include <stdio.h>
#include <string.h>

void reverseWord(char *word, int length)
{
    for (int i = 0; i < length / 2; i++)
    {
        char temp = word[i];
        word[i] = word[length - 1 - i];
        word[length - 1 - i] = temp;
    }
}

int main()
{
    int n;
    scanf("%d\n", &n);

    char sentence[1001];
    while (n--)
    {
        fgets(sentence, sizeof(sentence), stdin);
        sentence[strcspn(sentence, "\n")] = 0;

        char word[21];
        int wordLength = 0;

        for (int i = 0; sentence[i] != '\0'; i++)
        {
            if (sentence[i] == ' ' || sentence[i + 1] == '\0')
            {
                if (sentence[i + 1] == '\0')
                {
                    word[wordLength++] = sentence[i];
                }
                reverseWord(word, wordLength);
                printf("%s ", word);
                memset(word, 0, sizeof(word));
                wordLength = 0;
            }
            else
            {
                word[wordLength++] = sentence[i];
            }
        }
        printf("\n");
    }

    return 0;
}
