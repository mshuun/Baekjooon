#include <stdio.h>
#include <string.h>

int gcd(int a, int b)
{
    return b ? gcd(b, a % b) : a;
}

int is_repeated(const char *s, const char *pattern, int pattern_len)
{
    int len = strlen(s);
    if (len % pattern_len != 0)
        return 0;

    for (int i = 0; i < len; i++)
    {
        if (s[i] != pattern[i % pattern_len])
            return 0;
    }
    return 1;
}

int main()
{
    char S[51], T[51];
    scanf("%s %s", S, T);

    int lenS = strlen(S), lenT = strlen(T);
    int e = gcd(lenS, lenT);

    for (int i = 1; i <= e; i++)
    {
        if (e % i == 0 && is_repeated(S, S, i) && is_repeated(T, S, i))
        {
            S[i] = '\0';
            printf("%s", S);
            return 0;
        }
    }

    printf("No solution");
    return 0;
}
