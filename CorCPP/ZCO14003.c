#include <stdio.h>

int main(int argc, char const *argv[])
{
    long long int totalCust, tmp, max = 0, currev = 0;
    scanf("%lld", &totalCust);
    long long int budgets[totalCust];
    for (long long int i = 0; i < totalCust; i++)
    {
        scanf("%lld", &budgets[i]);
    }
    // for (long long int i = 0; i < totalCust; i++)
    // {
    //     printf("%lld ", budgets[i]);
    // }
    // printf("\n");
    for (long long int i = totalCust - 2; i >= 0; i--)
    {
        for (long long int j = 0; j <= i; j++)
        {
            if (budgets[j] > budgets[j + 1])
            {
                tmp = budgets[j];
                budgets[j] = budgets[j + 1];
                budgets[j + 1] = tmp;
            }
        }
    }
    // for (long long int i = 0; i < totalCust; i++)
    // {
    //     // printf("%lld ", budgets[i]);
    // }
    // printf("\n");

    for (long long int i = 0; i < totalCust; i++)
    {
        currev = budgets[i] * (totalCust - i);
        if (currev > max)
        {
            // printf("currev change %lld", currev);
            max = currev;
        }
    }
    printf("%lld", max);
    return 0;
}
