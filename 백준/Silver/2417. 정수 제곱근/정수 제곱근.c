#include <stdio.h>

int main()
{
    unsigned long long n, start, end, mid;
    scanf("%llu", &n);

    start = 0;
    end = pow(2.0, 32.0);
    if (n != 0)
        while (start <= end)
        {
            mid = (start + end) / 2;
            if (mid * mid < n)
            {
                start = mid + 1;
            }
            else
            {
                end = mid - 1;
            }
        }

    printf("%llu\n", start);
    return 0;
}
