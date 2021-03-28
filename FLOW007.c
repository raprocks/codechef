#include <stdio.h>

int main(int argc, char const *argv[])
{
    int testCases, input, rev = 0, cur;
    scanf("%d", &testCases);
    for (int i = 0; i < testCases; i++)
    {
        rev = 0;
        cur = 0;

        scanf("%d", &input);
        while (input != 0)
        {
            cur = input % 10;
            rev = (rev * 10) + cur;
            input /= 10;
            // printf("%d\n", rev);
        }
        printf("%d\n", rev);
    }

    return 0;
}
