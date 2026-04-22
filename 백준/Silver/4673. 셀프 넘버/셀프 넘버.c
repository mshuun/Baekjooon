#include <stdio.h>

int d(int n)
{
       int sum = n;
       while (n > 0)
       {
              sum += n % 10;
              n /= 10;
       }
       return sum;
}

void printSelfNumbers()
{
       int hasGenerator[10000] = {0};

       for (int i = 0; i < 10000; ++i)
       {
              int dn = d(i);
              if (dn < 10000)
              {
                     hasGenerator[dn] = 1;
              }
       }

       for (int i = 1; i < 10000; ++i)
       {
              if (!hasGenerator[i])
              {
                     printf("%d\n", i);
              }
       }
}

int main()
{
       printSelfNumbers();
       return 0;
}
