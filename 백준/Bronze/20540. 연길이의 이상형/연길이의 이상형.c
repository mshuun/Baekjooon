#include <stdio.h>
#include <string.h>

int main()
{
    char a[5];
    scanf("%4s", a);

    char result[5];
    for (int i = 0; i < 4; i++)
    {
        switch (a[i])
        {
        case 'I':
            result[i] = 'E';
            break;
        case 'E':
            result[i] = 'I';
            break;
        case 'N':
            result[i] = 'S';
            break;
        case 'S':
            result[i] = 'N';
            break;
        case 'T':
            result[i] = 'F';
            break;
        case 'F':
            result[i] = 'T';
            break;
        case 'J':
            result[i] = 'P';
            break;
        case 'P':
            result[i] = 'J';
            break;
        default:
            result[i] = a[i];
        }
    }
    result[4] = '\0';

    printf("%s", result);

    return 0;
}
