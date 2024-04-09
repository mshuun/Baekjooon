typedef long long L;
main(N, i)
{
    L T = 0;
    L r = 0;
    L a[200000];
    scanf("%d", &N);
    for (i = 0; i < N; i++)
    {
        scanf("%lld", &a[i]);
        T += a[i];
    }

    T /= N;
    N--;

    for (i = 0; i < N; i++)
    {
        L t = T - a[i];
        r += llabs(t);
        a[i + 1] -= t;
    }

    printf("%lld", r);
}
