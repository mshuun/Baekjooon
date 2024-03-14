#include <stdio.h>

int main()
{
    int x, y, s;
    while (1)
    {
        scanf("%d %d %d", &x, &y, &s);
        if (x == 0 && y == 0 && s == 0)
            break;

        int max_after_tax_price = 0;
        for (int before_tax_price1 = 1; before_tax_price1 < s; before_tax_price1++)
        {
            for (int before_tax_price2 = 1; before_tax_price2 < s; before_tax_price2++)
            {
                if (before_tax_price1 + before_tax_price2 + (before_tax_price1 * x / 100) + (before_tax_price2 * x / 100) == s)
                {
                    int after_tax_price1 = before_tax_price1 + (before_tax_price1 * y / 100);
                    int after_tax_price2 = before_tax_price2 + (before_tax_price2 * y / 100);
                    if (max_after_tax_price < after_tax_price1 + after_tax_price2)
                    {
                        max_after_tax_price = after_tax_price1 + after_tax_price2;
                    }
                }
            }
        }
        printf("%d\n", max_after_tax_price);
    }
    return 0;
}
