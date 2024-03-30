#include <stdio.h>

int main()
{
    int T, number, valid, count;
    for (scanf("%d", &T); T--; puts(valid == count % 2 ? "Valid" : "Corrupt"))
    {
        scanf("%d %d", &number, &valid);
        for (count = 0; number; count += number & 1, number >>= 1)
            ;
    }
    return 0;
}
