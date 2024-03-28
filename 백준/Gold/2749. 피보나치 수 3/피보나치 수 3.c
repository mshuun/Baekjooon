#include <stdio.h>

int main()
{
    long long n;
    scanf("%lld", &n);

    n = n % 1500000;
    long long a = 0;
    long long b = 1;
    for (int i = 0; i < n - 1; i++)
    {
        long long temp = b;
        b = (a + b) % 1000000;
        a = temp;
    }

    printf("%lld\n", b % 1500000);

    return 0;
}
