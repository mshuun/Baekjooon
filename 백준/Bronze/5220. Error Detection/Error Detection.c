#include <stdio.h>
int countOnes(int num)
{
    int count = 0;
    while (num)
    {
        count += num & 1;
        num >>= 1;
    }
    return count;
}

int main()
{
    int T, number, valid;
    scanf("%d", &T);
    for (int i = 0; i < T; i++)
    {
        scanf("%d %d", &number, &valid);
        if (valid == countOnes(number) % 2)
        {
            printf("Valid\n");
        }
        else
        {
            printf("Corrupt\n");
        }
    }
    return 0;
}
